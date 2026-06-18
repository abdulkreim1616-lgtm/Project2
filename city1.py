import asyncio
from mavsdk import System
from mavsdk.mission import MissionItem, MissionPlan

async def main():
    drone = System()
    print("Connecting to drone...")
    await drone.connect(system_address="udp://:14540")

    print("Waiting for drone to be ready and have GPS lock...")
    async for health in drone.telemetry.health():
        if health.is_global_position_ok and health.is_home_position_ok:
            print("Drone health OK!")
            break

    print("Arming drone...")
    await drone.action.arm()
    await asyncio.sleep(2)

    home = await anext(drone.telemetry.home())
    absolute_latitude = home.latitude_deg
    absolute_longitude = home.longitude_deg

    flying_alt = 15.0  
    speed = 4.0        

    METERS_TO_LAT = 9e-06
    METERS_TO_LON = 1.33e-05

    print("Defining relative mission waypoints around Gazebo cylinders...")

    mission_items = [
        MissionItem(
            absolute_latitude, absolute_longitude, flying_alt, speed, True,
            float('nan'), float('nan'), MissionItem.CameraAction.NONE,
            5.0,  
            float('nan'), 1.5, float('nan'), float('nan'), MissionItem.VehicleAction.NONE
        ),

        MissionItem(
            absolute_latitude + (-28.62) * METERS_TO_LAT, 
            absolute_longitude + (-9.29) * METERS_TO_LON, 
            flying_alt, speed, True,
            float('nan'), float('nan'), MissionItem.CameraAction.NONE,
            5.0,  
            float('nan'), 1.5, float('nan'), float('nan'), MissionItem.VehicleAction.NONE
        ),

        MissionItem(
            absolute_latitude + (-37.33) * METERS_TO_LAT, 
            absolute_longitude + (21.54) * METERS_TO_LON, 
            flying_alt, speed, True,
            float('nan'), float('nan'), MissionItem.CameraAction.NONE,
            5.0,  
            float('nan'), 1.5, float('nan'), float('nan'), MissionItem.VehicleAction.NONE
        ),

        MissionItem(
            absolute_latitude + (-3.85) * METERS_TO_LAT, 
            absolute_longitude + (21.48) * METERS_TO_LON, 
            flying_alt, speed, True,
            float('nan'), float('nan'), MissionItem.CameraAction.NONE,
            5.0,  
            float('nan'), 1.5, float('nan'), float('nan'), MissionItem.VehicleAction.NONE
        ),

        MissionItem(
            absolute_latitude, absolute_longitude, flying_alt, speed, True,
            float('nan'), float('nan'), MissionItem.CameraAction.NONE,
            2.0, float('nan'), 1.5, float('nan'), float('nan'), MissionItem.VehicleAction.NONE
        ),
    ]

    mission_plan = MissionPlan(mission_items)

    print("Clearing old missions from PX4...")
    await drone.mission.clear_mission()
    await asyncio.sleep(1)

    print("Uploading new relative mission...")
    await drone.mission.upload_mission(mission_plan)
    await asyncio.sleep(2)

    print("Starting mission...")
    await drone.mission.start_mission()
    await asyncio.sleep(1)

    async for mission_progress in drone.mission.mission_progress():
        print(f"Mission progress: Target Point {mission_progress.current + 1}/{mission_progress.total}")
        if mission_progress.current == mission_progress.total:
            print("-- Orbit completed around all cylinders!")
            break

    print("Initiating automatic landing on Helipad...")
    await drone.action.land()
    await asyncio.sleep(5)

if __name__ == "__main__":
    asyncio.run(main())