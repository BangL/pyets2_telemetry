SCS_CHANNELS = []
SCS_CONFIGS = []

class ScsChannel:
    def __init__(self, name, type, indexed):
        self.name = name
        self.type = type
        # Indicates if the value is indexed - not the channel
        self.indexed = indexed
        self.internal_id = len(SCS_CHANNELS)
        SCS_CHANNELS.append(self)

    def __eq__(self, other):
        return self.internal_id == other.internal_id

class ScsConfig:
    def __init__(self, id, type, indexed):
        self.id = id
        self.type = type
        # Indicates if the value is indexed
        self.indexed = indexed
        self.internal_id = len(SCS_CONFIGS)
        SCS_CONFIGS.append(self)

    def __eq__(self, other):
        return self.internal_id == other.internal_id
    
SCS_RESULT_ok = 0
SCS_RESULT_unsupported = -1
SCS_RESULT_invalid_parameter = -2
SCS_RESULT_already_registered = -3
SCS_RESULT_not_found = -4
SCS_RESULT_unsupported_type = -5
SCS_RESULT_not_now = -6
SCS_RESULT_generic_error = -7

SCS_TELEMETRY_CHANNEL_FLAG_none = 0x00000000
SCS_TELEMETRY_CHANNEL_FLAG_each_frame = 0x00000001
SCS_TELEMETRY_CHANNEL_FLAG_no_value = 0x00000002

SCS_U32_NIL = -1

SCS_VALUE_TYPE_INVALID = 0
SCS_VALUE_TYPE_bool = 1
SCS_VALUE_TYPE_s32 = 2
SCS_VALUE_TYPE_u32 = 3
SCS_VALUE_TYPE_u64 = 4
SCS_VALUE_TYPE_float = 5
SCS_VALUE_TYPE_double = 6
SCS_VALUE_TYPE_fvector = 7
SCS_VALUE_TYPE_dvector = 8
SCS_VALUE_TYPE_euler = 9
SCS_VALUE_TYPE_fplacement = 10
SCS_VALUE_TYPE_dplacement = 11
SCS_VALUE_TYPE_string = 12
SCS_VALUE_TYPE_s64 = 13

SCS_TELEMETRY_EVENT_invalid = 0
SCS_TELEMETRY_EVENT_frame_start = 1
SCS_TELEMETRY_EVENT_frame_end = 2
SCS_TELEMETRY_EVENT_paused = 3
SCS_TELEMETRY_EVENT_started = 4
SCS_TELEMETRY_EVENT_configuration = 5
SCS_TELEMETRY_EVENT_gameplay = 6

SCS_TELEMETRY_CHANNEL_game_time = ScsChannel('game.time', SCS_VALUE_TYPE_u32, False)
SCS_TELEMETRY_CHANNEL_local_scale = ScsChannel('local.scale', SCS_VALUE_TYPE_float, False)
SCS_TELEMETRY_CHANNEL_next_rest_stop = ScsChannel('rest.stop', SCS_VALUE_TYPE_s32, False)
SCS_TELEMETRY_JOB_CHANNEL_cargo_damage = ScsChannel('job.cargo.damage', SCS_VALUE_TYPE_float, False)
SCS_TELEMETRY_TRAILER_CHANNEL_cargo_damage = ScsChannel('trailer.cargo.damage', SCS_VALUE_TYPE_float, False)
SCS_TELEMETRY_TRAILER_CHANNEL_connected = ScsChannel('trailer.connected', SCS_VALUE_TYPE_bool, False)
SCS_TELEMETRY_TRAILER_CHANNEL_local_angular_acceleration = ScsChannel('trailer.acceleration.angular', SCS_VALUE_TYPE_fvector, False)
SCS_TELEMETRY_TRAILER_CHANNEL_local_angular_velocity = ScsChannel('trailer.velocity.angular', SCS_VALUE_TYPE_fvector, False)
SCS_TELEMETRY_TRAILER_CHANNEL_local_linear_acceleration = ScsChannel('trailer.acceleration.linear', SCS_VALUE_TYPE_fvector, False)
SCS_TELEMETRY_TRAILER_CHANNEL_local_linear_velocity = ScsChannel('trailer.velocity.linear', SCS_VALUE_TYPE_fvector, False)
SCS_TELEMETRY_TRAILER_CHANNEL_wear_chassis = ScsChannel('trailer.wear.chassis', SCS_VALUE_TYPE_float, False)
SCS_TELEMETRY_TRAILER_CHANNEL_wear_wheels = ScsChannel('trailer.wear.wheels', SCS_VALUE_TYPE_float, False)
SCS_TELEMETRY_TRAILER_CHANNEL_wheel_lift_offset = ScsChannel('trailer.wheel.lift.offset', SCS_VALUE_TYPE_float, False)
SCS_TELEMETRY_TRAILER_CHANNEL_wheel_lift = ScsChannel('trailer.wheel.lift', SCS_VALUE_TYPE_float, False)
SCS_TELEMETRY_TRAILER_CHANNEL_wheel_on_ground = ScsChannel('trailer.wheel.on_ground', SCS_VALUE_TYPE_bool, False)
SCS_TELEMETRY_TRAILER_CHANNEL_wheel_rotation = ScsChannel('trailer.wheel.rotation', SCS_VALUE_TYPE_float, False)
SCS_TELEMETRY_TRAILER_CHANNEL_wheel_steering = ScsChannel('trailer.wheel.steering', SCS_VALUE_TYPE_float, False)
SCS_TELEMETRY_TRAILER_CHANNEL_wheel_substance = ScsChannel('trailer.wheel.substance', SCS_VALUE_TYPE_u32, False)
SCS_TELEMETRY_TRAILER_CHANNEL_wheel_susp_deflection = ScsChannel('trailer.wheel.suspension.deflection', SCS_VALUE_TYPE_float, False)
SCS_TELEMETRY_TRAILER_CHANNEL_wheel_velocity = ScsChannel('trailer.wheel.angular_velocity', SCS_VALUE_TYPE_fvector, False)
SCS_TELEMETRY_TRAILER_CHANNEL_world_placement = ScsChannel('trailer.world.placement', SCS_VALUE_TYPE_dplacement, False)
# Not available? Getting SCS_RESULT_not_found
#SCS_TELEMETRY_TRUCK_CHANNEL_adblue_average_consumption = ScsChannel('truck.adblue.consumption.average', SCS_VALUE_TYPE_float, False)
SCS_TELEMETRY_TRUCK_CHANNEL_adblue = ScsChannel('truck.adblue', SCS_VALUE_TYPE_float, False)
SCS_TELEMETRY_TRUCK_CHANNEL_adblue_warning = ScsChannel('truck.adblue.warning', SCS_VALUE_TYPE_bool, False)
SCS_TELEMETRY_TRUCK_CHANNEL_battery_voltage = ScsChannel('truck.battery.voltage', SCS_VALUE_TYPE_float, False)
SCS_TELEMETRY_TRUCK_CHANNEL_battery_voltage_warning = ScsChannel('truck.battery.voltage.warning', SCS_VALUE_TYPE_bool, False)
SCS_TELEMETRY_TRUCK_CHANNEL_brake_air_pressure_emergency = ScsChannel('truck.brake.air.pressure.emergency', SCS_VALUE_TYPE_bool, False)
SCS_TELEMETRY_TRUCK_CHANNEL_brake_air_pressure = ScsChannel('truck.brake.air.pressure', SCS_VALUE_TYPE_float, False)
SCS_TELEMETRY_TRUCK_CHANNEL_brake_air_pressure_warning = ScsChannel('truck.brake.air.pressure.warning', SCS_VALUE_TYPE_bool, False)
SCS_TELEMETRY_TRUCK_CHANNEL_brake_temperature = ScsChannel('truck.brake.temperature', SCS_VALUE_TYPE_float, False)
SCS_TELEMETRY_TRUCK_CHANNEL_cabin_angular_acceleration = ScsChannel('truck.cabin.acceleration.angular', SCS_VALUE_TYPE_fvector, False)
SCS_TELEMETRY_TRUCK_CHANNEL_cabin_angular_velocity = ScsChannel('truck.cabin.velocity.angular', SCS_VALUE_TYPE_fvector, False)
SCS_TELEMETRY_TRUCK_CHANNEL_cabin_offset = ScsChannel('truck.cabin.offset', SCS_VALUE_TYPE_fplacement, False)
SCS_TELEMETRY_TRUCK_CHANNEL_cruise_control = ScsChannel('truck.cruise_control', SCS_VALUE_TYPE_float, False)
SCS_TELEMETRY_TRUCK_CHANNEL_dashboard_backlight = ScsChannel('truck.dashboard.backlight', SCS_VALUE_TYPE_float, False)
SCS_TELEMETRY_TRUCK_CHANNEL_displayed_gear = ScsChannel('truck.displayed.gear', SCS_VALUE_TYPE_s32, False)
SCS_TELEMETRY_TRUCK_CHANNEL_effective_brake = ScsChannel('truck.effective.brake', SCS_VALUE_TYPE_float, False)
SCS_TELEMETRY_TRUCK_CHANNEL_effective_clutch = ScsChannel('truck.effective.clutch', SCS_VALUE_TYPE_float, False)
SCS_TELEMETRY_TRUCK_CHANNEL_effective_steering = ScsChannel('truck.effective.steering', SCS_VALUE_TYPE_float, False)
SCS_TELEMETRY_TRUCK_CHANNEL_effective_throttle = ScsChannel('truck.effective.throttle', SCS_VALUE_TYPE_float, False)
SCS_TELEMETRY_TRUCK_CHANNEL_electric_enabled = ScsChannel('truck.electric.enabled', SCS_VALUE_TYPE_bool, False)
SCS_TELEMETRY_TRUCK_CHANNEL_engine_enabled = ScsChannel('truck.engine.enabled', SCS_VALUE_TYPE_bool, False)
SCS_TELEMETRY_TRUCK_CHANNEL_engine_gear = ScsChannel('truck.engine.gear', SCS_VALUE_TYPE_s32, False)
SCS_TELEMETRY_TRUCK_CHANNEL_engine_rpm = ScsChannel('truck.engine.rpm', SCS_VALUE_TYPE_float, False)
SCS_TELEMETRY_TRUCK_CHANNEL_fuel_average_consumption = ScsChannel('truck.fuel.consumption.average', SCS_VALUE_TYPE_float, False)
SCS_TELEMETRY_TRUCK_CHANNEL_fuel_range = ScsChannel('truck.fuel.range', SCS_VALUE_TYPE_float, False)
SCS_TELEMETRY_TRUCK_CHANNEL_fuel = ScsChannel('truck.fuel.amount', SCS_VALUE_TYPE_float, False)
SCS_TELEMETRY_TRUCK_CHANNEL_fuel_warning = ScsChannel('truck.fuel.warning', SCS_VALUE_TYPE_bool, False)
SCS_TELEMETRY_TRUCK_CHANNEL_head_offset = ScsChannel('truck.head.offset', SCS_VALUE_TYPE_fplacement, False)
SCS_TELEMETRY_TRUCK_CHANNEL_hshifter_selector = ScsChannel('truck.hshifter.select', SCS_VALUE_TYPE_bool, True)
SCS_TELEMETRY_TRUCK_CHANNEL_hshifter_slot = ScsChannel('truck.hshifter.slot', SCS_VALUE_TYPE_u32, False)
SCS_TELEMETRY_TRUCK_CHANNEL_input_brake = ScsChannel('truck.input.brake', SCS_VALUE_TYPE_float, False)
SCS_TELEMETRY_TRUCK_CHANNEL_input_clutch = ScsChannel('truck.input.clutch', SCS_VALUE_TYPE_float, False)
SCS_TELEMETRY_TRUCK_CHANNEL_input_steering = ScsChannel('truck.input.steering', SCS_VALUE_TYPE_float, False)
SCS_TELEMETRY_TRUCK_CHANNEL_input_throttle = ScsChannel('truck.input.throttle', SCS_VALUE_TYPE_float, False)
SCS_TELEMETRY_TRUCK_CHANNEL_lblinker = ScsChannel('truck.lblinker', SCS_VALUE_TYPE_bool, False)
SCS_TELEMETRY_TRUCK_CHANNEL_light_aux_front = ScsChannel('truck.light.aux.front', SCS_VALUE_TYPE_u32, False)
SCS_TELEMETRY_TRUCK_CHANNEL_light_aux_roof = ScsChannel('truck.light.aux.roof', SCS_VALUE_TYPE_u32, False)
SCS_TELEMETRY_TRUCK_CHANNEL_light_beacon = ScsChannel('truck.light.beacon', SCS_VALUE_TYPE_bool, False)
SCS_TELEMETRY_TRUCK_CHANNEL_light_brake = ScsChannel('truck.light.brake', SCS_VALUE_TYPE_bool, False)
SCS_TELEMETRY_TRUCK_CHANNEL_light_high_beam = ScsChannel('truck.light.beam.high', SCS_VALUE_TYPE_bool, False)
SCS_TELEMETRY_TRUCK_CHANNEL_light_lblinker = ScsChannel('truck.light.lblinker', SCS_VALUE_TYPE_bool, False)
SCS_TELEMETRY_TRUCK_CHANNEL_light_low_beam = ScsChannel('truck.light.beam.low', SCS_VALUE_TYPE_bool, False)
SCS_TELEMETRY_TRUCK_CHANNEL_light_parking = ScsChannel('truck.light.parking', SCS_VALUE_TYPE_bool, False)
SCS_TELEMETRY_TRUCK_CHANNEL_light_rblinker = ScsChannel('truck.light.rblinker', SCS_VALUE_TYPE_bool, False)
SCS_TELEMETRY_TRUCK_CHANNEL_light_reverse = ScsChannel('truck.light.reverse', SCS_VALUE_TYPE_bool, False)
SCS_TELEMETRY_TRUCK_CHANNEL_local_angular_acceleration = ScsChannel('truck.local.acceleration.angular', SCS_VALUE_TYPE_fvector, False)
SCS_TELEMETRY_TRUCK_CHANNEL_local_angular_velocity = ScsChannel('truck.local.velocity.angular', SCS_VALUE_TYPE_fvector, False)
SCS_TELEMETRY_TRUCK_CHANNEL_local_linear_acceleration = ScsChannel('truck.local.acceleration.linear', SCS_VALUE_TYPE_fvector, False)
SCS_TELEMETRY_TRUCK_CHANNEL_local_linear_velocity = ScsChannel('truck.local.velocity.linear', SCS_VALUE_TYPE_fvector, False)
SCS_TELEMETRY_TRUCK_CHANNEL_motor_brake = ScsChannel('truck.brake.motor', SCS_VALUE_TYPE_bool, False)
SCS_TELEMETRY_TRUCK_CHANNEL_navigation_distance = ScsChannel('truck.navigation.distance', SCS_VALUE_TYPE_float, False)
SCS_TELEMETRY_TRUCK_CHANNEL_navigation_speed_limit = ScsChannel('truck.navigation.speed.limit', SCS_VALUE_TYPE_float, False)
SCS_TELEMETRY_TRUCK_CHANNEL_navigation_time = ScsChannel('truck.navigation.time', SCS_VALUE_TYPE_float, False)
SCS_TELEMETRY_TRUCK_CHANNEL_odometer = ScsChannel('truck.odometer', SCS_VALUE_TYPE_float, False)
SCS_TELEMETRY_TRUCK_CHANNEL_oil_pressure = ScsChannel('truck.oil.pressure', SCS_VALUE_TYPE_float, False)
SCS_TELEMETRY_TRUCK_CHANNEL_oil_pressure_warning = ScsChannel('truck.oil.pressure.warning', SCS_VALUE_TYPE_bool, False)
SCS_TELEMETRY_TRUCK_CHANNEL_oil_temperature = ScsChannel('truck.oil.temperature', SCS_VALUE_TYPE_float, False)
SCS_TELEMETRY_TRUCK_CHANNEL_parking_brake = ScsChannel('truck.brake.parking', SCS_VALUE_TYPE_bool, False)
SCS_TELEMETRY_TRUCK_CHANNEL_rblinker = ScsChannel('truck.rblinker', SCS_VALUE_TYPE_bool, False)
SCS_TELEMETRY_TRUCK_CHANNEL_retarder_level = ScsChannel('truck.brake.retarder', SCS_VALUE_TYPE_u32, False)
SCS_TELEMETRY_TRUCK_CHANNEL_speed = ScsChannel('truck.speed', SCS_VALUE_TYPE_float, False)
SCS_TELEMETRY_TRUCK_CHANNEL_water_temperature = ScsChannel('truck.water.temperature', SCS_VALUE_TYPE_float, False)
SCS_TELEMETRY_TRUCK_CHANNEL_water_temperature_warning = ScsChannel('truck.water.temperature.warning', SCS_VALUE_TYPE_bool, False)
SCS_TELEMETRY_TRUCK_CHANNEL_wear_cabin = ScsChannel('truck.wear.cabin', SCS_VALUE_TYPE_float, False)
SCS_TELEMETRY_TRUCK_CHANNEL_wear_chassis = ScsChannel('truck.wear.chassis', SCS_VALUE_TYPE_float, False)
SCS_TELEMETRY_TRUCK_CHANNEL_wear_engine = ScsChannel('truck.wear.engine', SCS_VALUE_TYPE_float, False)
SCS_TELEMETRY_TRUCK_CHANNEL_wear_transmission = ScsChannel('truck.wear.transmission', SCS_VALUE_TYPE_float, False)
SCS_TELEMETRY_TRUCK_CHANNEL_wear_wheels = ScsChannel('truck.wear.wheels', SCS_VALUE_TYPE_float, False)
SCS_TELEMETRY_TRUCK_CHANNEL_wheel_lift_offset = ScsChannel('truck.wheel.lift.offset', SCS_VALUE_TYPE_float, True)
SCS_TELEMETRY_TRUCK_CHANNEL_wheel_lift = ScsChannel('truck.wheel.lift', SCS_VALUE_TYPE_float, True)
SCS_TELEMETRY_TRUCK_CHANNEL_wheel_on_ground = ScsChannel('truck.wheel.on_ground', SCS_VALUE_TYPE_bool, True)
SCS_TELEMETRY_TRUCK_CHANNEL_wheel_rotation = ScsChannel('truck.wheel.rotation', SCS_VALUE_TYPE_float, True)
SCS_TELEMETRY_TRUCK_CHANNEL_wheel_steering = ScsChannel('truck.wheel.steering', SCS_VALUE_TYPE_float, True)
SCS_TELEMETRY_TRUCK_CHANNEL_wheel_substance = ScsChannel('truck.wheel.substance', SCS_VALUE_TYPE_u32, True)
SCS_TELEMETRY_TRUCK_CHANNEL_wheel_susp_deflection = ScsChannel('truck.wheel.suspension.deflection', SCS_VALUE_TYPE_float, True)
SCS_TELEMETRY_TRUCK_CHANNEL_wheel_velocity = ScsChannel('truck.wheel.angular_velocity', SCS_VALUE_TYPE_float, True)
SCS_TELEMETRY_TRUCK_CHANNEL_wipers = ScsChannel('truck.wipers', SCS_VALUE_TYPE_bool, False)
SCS_TELEMETRY_TRUCK_CHANNEL_world_placement = ScsChannel('truck.world.placement', SCS_VALUE_TYPE_dplacement, False)

SCS_TELEMETRY_CONFIG_controls = 'controls'
SCS_TELEMETRY_CONFIG_hshifter = 'hshifter'
SCS_TELEMETRY_CONFIG_job = 'job'
SCS_TELEMETRY_CONFIG_substances = 'substances'
SCS_TELEMETRY_CONFIG_trailer = 'trailer'
SCS_TELEMETRY_CONFIG_truck = 'truck'

SCS_TELEMETRY_CONFIG_ATTRIBUTE_adblue_capacity = 'adblue.capacity'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_adblue_warning_factor = 'adblue.warning.factor'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_air_pressure_emergency = 'brake.air.pressure.emergency'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_air_pressure_warning = 'brake.air.pressure.warning'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_battery_voltage_warning = 'battery.voltage.warning'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_body_type = 'body.type'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_brand_id = 'brand_id'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_brand = 'brand'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_cabin_position = 'cabin.position'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_cargo_accessory_id = 'cargo.accessory.id'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_cargo_id = 'cargo.id'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_cargo_mass = 'cargo.mass'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_cargo = 'cargo'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_cargo_unit_count = 'cargo.unit.count'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_cargo_unit_mass = 'cargo.unit.mass'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_chain_type = 'chain.type'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_delivery_time = 'delivery.time'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_destination_city_id = 'destination.city.id'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_destination_city = 'destination.city'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_destination_company_id = 'destination.company.id'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_destination_company = 'destination.company'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_differential_ratio = 'differential.ratio'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_forward_gear_count = 'gears.forward'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_forward_ratio = 'forward.ratio'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_fuel_capacity = 'fuel.capacity'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_fuel_warning_factor = 'fuel.warning.factor'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_head_position = 'head.position'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_hook_position = 'hook.position'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_id = 'id'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_income = 'income'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_is_cargo_loaded = 'cargo.loaded'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_job_market = 'job.market'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_license_plate_country_id = 'license.plate.country.id'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_license_plate_country = 'license.plate.country'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_license_plate = 'license.plate'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_name = 'name'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_oil_pressure_warning = 'oil.pressure.warning'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_retarder_step_count = 'retarder.steps'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_reverse_gear_count = 'gears.reverse'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_reverse_ratio = 'reverse.ratio'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_rpm_limit = 'rpm.limit'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_selector_count = 'selector.count'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_shifter_type = 'shifter.type'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_slot_gear = 'slot.gear'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_slot_handle_position = 'slot.handle.position'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_slot_selectors = 'slot.selectors'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_source_city_id = 'source.city.id'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_source_city = 'source.city'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_source_company_id = 'source.company.id'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_source_company = 'source.company'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_special_job = 'is.special.job'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_water_temperature_warning = 'water.temperature.warning'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_wheel_count = 'wheels.count'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_wheel_liftable = 'wheel.liftable'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_wheel_position = 'wheel.position'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_wheel_powered = 'wheel.powered'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_wheel_radius = 'wheel.radius'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_wheel_simulated = 'wheel.simulated'
SCS_TELEMETRY_CONFIG_ATTRIBUTE_wheel_steerable = 'wheel.steerable'
