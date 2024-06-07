#
# Copyright 2019 Thomas Axelsson <thomasa88@gmail.com>
#
# This file is part of pyets2_telemetry.
#
# pyets2_telemetry is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyets2_telemetry is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pyets2_telemetry.  If not, see <https://www.gnu.org/licenses/>.
#

SCS_CHANNELS = []

class ScsObjectBase(object):
    def __init__(self, internal_id):
        self.internal_id: int | str = internal_id

    def __eq__(self, other) -> bool:
        return self.internal_id == other.internal_id

    def __hash__(self) -> int | str:
        return self.internal_id

class ScsChannelBase(ScsObjectBase):
    def __init__(self, internal_id, name, type, indexed=False, index_count=1):
        super().__init__(internal_id)
        self.name: str = name
        self.type: int = type
        self.indexed: bool = indexed
        self.index_count: int = index_count

class ScsChannel(ScsChannelBase):
    def __init__(self, name, type, indexed=False, index_count=1, parent=None):
        super().__init__(len(SCS_CHANNELS), name, type, indexed, index_count)
        self.parent: ScsIndexedChannel | None = parent
        SCS_CHANNELS.append(self)

class ScsIndexedChannel(ScsChannelBase):
    def __init__(self, root, name, type, count, indexed=False, index_count=1):
        super().__init__(name, name, type, indexed, index_count)
        self.channels: list[ScsChannel] = []
        for i in list(range(count)):
            self.channels.append(ScsChannel(root + '.' + str(i) + '.' + name, type, indexed, index_count, self))

SCS_ATTRIBUTES = {}

class ScsAttribute(ScsObjectBase):
    def __init__(self, name, indexed=False, index_count=1):
        super().__init__(name)
        self.name: str = name
        self.indexed: bool = indexed
        self.index_count: int = index_count
        SCS_ATTRIBUTES[name] = self

class ScsEvent(ScsObjectBase):
    def __init__(self, id):
        super().__init__(id)
        self.id: str = id

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

SCS_TELEMETRY_wheels_count = 14
SCS_TELEMETRY_trailers_count = 10

SCS_TELEMETRY_CHANNEL_game_time = ScsChannel('game.time', SCS_VALUE_TYPE_u32)
SCS_TELEMETRY_CHANNEL_local_scale = ScsChannel('local.scale', SCS_VALUE_TYPE_float)
SCS_TELEMETRY_CHANNEL_multiplayer_time_offset = ScsChannel('multiplayer.time.offset', SCS_VALUE_TYPE_s32)
SCS_TELEMETRY_CHANNEL_next_rest_stop = ScsChannel('rest.stop', SCS_VALUE_TYPE_s32)

SCS_TELEMETRY_JOB_CHANNEL_cargo_damage = ScsChannel('job.cargo.damage', SCS_VALUE_TYPE_float)

SCS_TELEMETRY_TRAILER_CHANNEL_cargo_damage = ScsIndexedChannel('trailer', 'cargo.damage', SCS_VALUE_TYPE_float, SCS_TELEMETRY_trailers_count)
SCS_TELEMETRY_TRAILER_CHANNEL_connected = ScsIndexedChannel('trailer', 'connected', SCS_VALUE_TYPE_bool, SCS_TELEMETRY_trailers_count)
SCS_TELEMETRY_TRAILER_CHANNEL_local_angular_acceleration = ScsIndexedChannel('trailer', 'acceleration.angular', SCS_VALUE_TYPE_fvector, SCS_TELEMETRY_trailers_count)
SCS_TELEMETRY_TRAILER_CHANNEL_local_angular_velocity = ScsIndexedChannel('trailer', 'velocity.angular', SCS_VALUE_TYPE_fvector, SCS_TELEMETRY_trailers_count)
SCS_TELEMETRY_TRAILER_CHANNEL_local_linear_acceleration = ScsIndexedChannel('trailer', 'acceleration.linear', SCS_VALUE_TYPE_fvector, SCS_TELEMETRY_trailers_count)
SCS_TELEMETRY_TRAILER_CHANNEL_local_linear_velocity = ScsIndexedChannel('trailer', 'velocity.linear', SCS_VALUE_TYPE_fvector, SCS_TELEMETRY_trailers_count)
SCS_TELEMETRY_TRAILER_CHANNEL_wear_body = ScsIndexedChannel('trailer', 'wear.body', SCS_VALUE_TYPE_float, SCS_TELEMETRY_trailers_count)
SCS_TELEMETRY_TRAILER_CHANNEL_wear_chassis = ScsIndexedChannel('trailer', 'wear.chassis', SCS_VALUE_TYPE_float, SCS_TELEMETRY_trailers_count)
SCS_TELEMETRY_TRAILER_CHANNEL_wear_wheels = ScsIndexedChannel('trailer', 'wear.wheels', SCS_VALUE_TYPE_float, SCS_TELEMETRY_trailers_count)
SCS_TELEMETRY_TRAILER_CHANNEL_wheel_lift_offset = ScsIndexedChannel('trailer', 'wheel.lift.offset', SCS_VALUE_TYPE_float, SCS_TELEMETRY_trailers_count, True, SCS_TELEMETRY_wheels_count) # indexed
SCS_TELEMETRY_TRAILER_CHANNEL_wheel_lift = ScsIndexedChannel('trailer', 'wheel.lift', SCS_VALUE_TYPE_float, SCS_TELEMETRY_trailers_count, True, SCS_TELEMETRY_wheels_count) # indexed
SCS_TELEMETRY_TRAILER_CHANNEL_wheel_on_ground = ScsIndexedChannel('trailer', 'wheel.on_ground', SCS_VALUE_TYPE_bool, SCS_TELEMETRY_trailers_count, True, SCS_TELEMETRY_wheels_count) # indexed
SCS_TELEMETRY_TRAILER_CHANNEL_wheel_rotation = ScsIndexedChannel('trailer', 'wheel.rotation', SCS_VALUE_TYPE_float, SCS_TELEMETRY_trailers_count, True, SCS_TELEMETRY_wheels_count) # indexed
SCS_TELEMETRY_TRAILER_CHANNEL_wheel_steering = ScsIndexedChannel('trailer', 'wheel.steering', SCS_VALUE_TYPE_float, SCS_TELEMETRY_trailers_count, True, SCS_TELEMETRY_wheels_count) # indexed
SCS_TELEMETRY_TRAILER_CHANNEL_wheel_substance = ScsIndexedChannel('trailer', 'wheel.substance', SCS_VALUE_TYPE_u32, SCS_TELEMETRY_trailers_count, True, SCS_TELEMETRY_wheels_count) # indexed
SCS_TELEMETRY_TRAILER_CHANNEL_wheel_susp_deflection = ScsIndexedChannel('trailer', 'wheel.suspension.deflection', SCS_VALUE_TYPE_float, SCS_TELEMETRY_trailers_count, True, SCS_TELEMETRY_wheels_count) # indexed
SCS_TELEMETRY_TRAILER_CHANNEL_wheel_velocity = ScsIndexedChannel('trailer', 'wheel.angular_velocity', SCS_VALUE_TYPE_fvector, SCS_TELEMETRY_trailers_count, True, SCS_TELEMETRY_wheels_count) # indexed
SCS_TELEMETRY_TRAILER_CHANNEL_world_placement = ScsIndexedChannel('trailer', 'world.placement', SCS_VALUE_TYPE_dplacement, SCS_TELEMETRY_trailers_count)

# SCS_TELEMETRY_TRUCK_CHANNEL_adblue_average_consumption = ScsChannel('truck.adblue.consumption.average', SCS_VALUE_TYPE_float) // Removed in SDK 1.9
SCS_TELEMETRY_TRUCK_CHANNEL_adblue = ScsChannel('truck.adblue', SCS_VALUE_TYPE_float)
SCS_TELEMETRY_TRUCK_CHANNEL_adblue_warning = ScsChannel('truck.adblue.warning', SCS_VALUE_TYPE_bool)
SCS_TELEMETRY_TRUCK_CHANNEL_battery_voltage = ScsChannel('truck.battery.voltage', SCS_VALUE_TYPE_float)
SCS_TELEMETRY_TRUCK_CHANNEL_battery_voltage_warning = ScsChannel('truck.battery.voltage.warning', SCS_VALUE_TYPE_bool)
SCS_TELEMETRY_TRUCK_CHANNEL_brake_air_pressure_emergency = ScsChannel('truck.brake.air.pressure.emergency', SCS_VALUE_TYPE_bool)
SCS_TELEMETRY_TRUCK_CHANNEL_brake_air_pressure = ScsChannel('truck.brake.air.pressure', SCS_VALUE_TYPE_float)
SCS_TELEMETRY_TRUCK_CHANNEL_brake_air_pressure_warning = ScsChannel('truck.brake.air.pressure.warning', SCS_VALUE_TYPE_bool)
SCS_TELEMETRY_TRUCK_CHANNEL_brake_temperature = ScsChannel('truck.brake.temperature', SCS_VALUE_TYPE_float)
SCS_TELEMETRY_TRUCK_CHANNEL_cabin_angular_acceleration = ScsChannel('truck.cabin.acceleration.angular', SCS_VALUE_TYPE_fvector)
SCS_TELEMETRY_TRUCK_CHANNEL_cabin_angular_velocity = ScsChannel('truck.cabin.velocity.angular', SCS_VALUE_TYPE_fvector)
SCS_TELEMETRY_TRUCK_CHANNEL_cabin_offset = ScsChannel('truck.cabin.offset', SCS_VALUE_TYPE_fplacement)
SCS_TELEMETRY_TRUCK_CHANNEL_cruise_control = ScsChannel('truck.cruise_control', SCS_VALUE_TYPE_float)
SCS_TELEMETRY_TRUCK_CHANNEL_dashboard_backlight = ScsChannel('truck.dashboard.backlight', SCS_VALUE_TYPE_float)
SCS_TELEMETRY_TRUCK_CHANNEL_differential_lock = ScsChannel('truck.differential_lock', SCS_VALUE_TYPE_bool)
SCS_TELEMETRY_TRUCK_CHANNEL_lift_axle = ScsChannel('truck.lift_axle', SCS_VALUE_TYPE_bool)
SCS_TELEMETRY_TRUCK_CHANNEL_lift_axle_indicator = ScsChannel('truck.lift_axle.indicator', SCS_VALUE_TYPE_bool)
SCS_TELEMETRY_TRUCK_CHANNEL_trailer_lift_axle = ScsChannel('truck.trailer.lift_axle', SCS_VALUE_TYPE_bool)
SCS_TELEMETRY_TRUCK_CHANNEL_trailer_lift_axle_indicator = ScsChannel('truck.trailer.lift_axle.indicator', SCS_VALUE_TYPE_bool)
SCS_TELEMETRY_TRUCK_CHANNEL_displayed_gear = ScsChannel('truck.displayed.gear', SCS_VALUE_TYPE_s32)
SCS_TELEMETRY_TRUCK_CHANNEL_effective_brake = ScsChannel('truck.effective.brake', SCS_VALUE_TYPE_float)
SCS_TELEMETRY_TRUCK_CHANNEL_effective_clutch = ScsChannel('truck.effective.clutch', SCS_VALUE_TYPE_float)
SCS_TELEMETRY_TRUCK_CHANNEL_effective_steering = ScsChannel('truck.effective.steering', SCS_VALUE_TYPE_float)
SCS_TELEMETRY_TRUCK_CHANNEL_effective_throttle = ScsChannel('truck.effective.throttle', SCS_VALUE_TYPE_float)
SCS_TELEMETRY_TRUCK_CHANNEL_electric_enabled = ScsChannel('truck.electric.enabled', SCS_VALUE_TYPE_bool)
SCS_TELEMETRY_TRUCK_CHANNEL_engine_enabled = ScsChannel('truck.engine.enabled', SCS_VALUE_TYPE_bool)
SCS_TELEMETRY_TRUCK_CHANNEL_engine_gear = ScsChannel('truck.engine.gear', SCS_VALUE_TYPE_s32)
SCS_TELEMETRY_TRUCK_CHANNEL_engine_rpm = ScsChannel('truck.engine.rpm', SCS_VALUE_TYPE_float)
SCS_TELEMETRY_TRUCK_CHANNEL_fuel_average_consumption = ScsChannel('truck.fuel.consumption.average', SCS_VALUE_TYPE_float)
SCS_TELEMETRY_TRUCK_CHANNEL_fuel_range = ScsChannel('truck.fuel.range', SCS_VALUE_TYPE_float)
SCS_TELEMETRY_TRUCK_CHANNEL_fuel = ScsChannel('truck.fuel.amount', SCS_VALUE_TYPE_float)
SCS_TELEMETRY_TRUCK_CHANNEL_fuel_warning = ScsChannel('truck.fuel.warning', SCS_VALUE_TYPE_bool)
SCS_TELEMETRY_TRUCK_CHANNEL_head_offset = ScsChannel('truck.head.offset', SCS_VALUE_TYPE_fplacement)
SCS_TELEMETRY_TRUCK_CHANNEL_hshifter_selector = ScsChannel('truck.hshifter.select', SCS_VALUE_TYPE_bool, True, 2) # indexed
SCS_TELEMETRY_TRUCK_CHANNEL_hshifter_slot = ScsChannel('truck.hshifter.slot', SCS_VALUE_TYPE_u32)
SCS_TELEMETRY_TRUCK_CHANNEL_input_brake = ScsChannel('truck.input.brake', SCS_VALUE_TYPE_float)
SCS_TELEMETRY_TRUCK_CHANNEL_input_clutch = ScsChannel('truck.input.clutch', SCS_VALUE_TYPE_float)
SCS_TELEMETRY_TRUCK_CHANNEL_input_steering = ScsChannel('truck.input.steering', SCS_VALUE_TYPE_float)
SCS_TELEMETRY_TRUCK_CHANNEL_input_throttle = ScsChannel('truck.input.throttle', SCS_VALUE_TYPE_float)
SCS_TELEMETRY_TRUCK_CHANNEL_lblinker = ScsChannel('truck.lblinker', SCS_VALUE_TYPE_bool)
SCS_TELEMETRY_TRUCK_CHANNEL_light_aux_front = ScsChannel('truck.light.aux.front', SCS_VALUE_TYPE_u32)
SCS_TELEMETRY_TRUCK_CHANNEL_light_aux_roof = ScsChannel('truck.light.aux.roof', SCS_VALUE_TYPE_u32)
SCS_TELEMETRY_TRUCK_CHANNEL_light_beacon = ScsChannel('truck.light.beacon', SCS_VALUE_TYPE_bool)
SCS_TELEMETRY_TRUCK_CHANNEL_light_brake = ScsChannel('truck.light.brake', SCS_VALUE_TYPE_bool)
SCS_TELEMETRY_TRUCK_CHANNEL_light_high_beam = ScsChannel('truck.light.beam.high', SCS_VALUE_TYPE_bool)
SCS_TELEMETRY_TRUCK_CHANNEL_light_lblinker = ScsChannel('truck.light.lblinker', SCS_VALUE_TYPE_bool)
SCS_TELEMETRY_TRUCK_CHANNEL_light_low_beam = ScsChannel('truck.light.beam.low', SCS_VALUE_TYPE_bool)
SCS_TELEMETRY_TRUCK_CHANNEL_light_parking = ScsChannel('truck.light.parking', SCS_VALUE_TYPE_bool)
SCS_TELEMETRY_TRUCK_CHANNEL_light_rblinker = ScsChannel('truck.light.rblinker', SCS_VALUE_TYPE_bool)
SCS_TELEMETRY_TRUCK_CHANNEL_light_reverse = ScsChannel('truck.light.reverse', SCS_VALUE_TYPE_bool)
SCS_TELEMETRY_TRUCK_CHANNEL_local_angular_acceleration = ScsChannel('truck.local.acceleration.angular', SCS_VALUE_TYPE_fvector)
SCS_TELEMETRY_TRUCK_CHANNEL_local_angular_velocity = ScsChannel('truck.local.velocity.angular', SCS_VALUE_TYPE_fvector)
SCS_TELEMETRY_TRUCK_CHANNEL_local_linear_acceleration = ScsChannel('truck.local.acceleration.linear', SCS_VALUE_TYPE_fvector)
SCS_TELEMETRY_TRUCK_CHANNEL_local_linear_velocity = ScsChannel('truck.local.velocity.linear', SCS_VALUE_TYPE_fvector)
SCS_TELEMETRY_TRUCK_CHANNEL_motor_brake = ScsChannel('truck.brake.motor', SCS_VALUE_TYPE_bool)
SCS_TELEMETRY_TRUCK_CHANNEL_navigation_distance = ScsChannel('truck.navigation.distance', SCS_VALUE_TYPE_float)
SCS_TELEMETRY_TRUCK_CHANNEL_navigation_speed_limit = ScsChannel('truck.navigation.speed.limit', SCS_VALUE_TYPE_float)
SCS_TELEMETRY_TRUCK_CHANNEL_navigation_time = ScsChannel('truck.navigation.time', SCS_VALUE_TYPE_float)
SCS_TELEMETRY_TRUCK_CHANNEL_odometer = ScsChannel('truck.odometer', SCS_VALUE_TYPE_float)
SCS_TELEMETRY_TRUCK_CHANNEL_oil_pressure = ScsChannel('truck.oil.pressure', SCS_VALUE_TYPE_float)
SCS_TELEMETRY_TRUCK_CHANNEL_oil_pressure_warning = ScsChannel('truck.oil.pressure.warning', SCS_VALUE_TYPE_bool)
SCS_TELEMETRY_TRUCK_CHANNEL_oil_temperature = ScsChannel('truck.oil.temperature', SCS_VALUE_TYPE_float)
SCS_TELEMETRY_TRUCK_CHANNEL_parking_brake = ScsChannel('truck.brake.parking', SCS_VALUE_TYPE_bool)
SCS_TELEMETRY_TRUCK_CHANNEL_rblinker = ScsChannel('truck.rblinker', SCS_VALUE_TYPE_bool)
SCS_TELEMETRY_TRUCK_CHANNEL_hazard_warning = ScsChannel('truck.hazard.warning', SCS_VALUE_TYPE_bool)
SCS_TELEMETRY_TRUCK_CHANNEL_retarder_level = ScsChannel('truck.brake.retarder', SCS_VALUE_TYPE_u32)
SCS_TELEMETRY_TRUCK_CHANNEL_speed = ScsChannel('truck.speed', SCS_VALUE_TYPE_float)
SCS_TELEMETRY_TRUCK_CHANNEL_water_temperature = ScsChannel('truck.water.temperature', SCS_VALUE_TYPE_float)
SCS_TELEMETRY_TRUCK_CHANNEL_water_temperature_warning = ScsChannel('truck.water.temperature.warning', SCS_VALUE_TYPE_bool)
SCS_TELEMETRY_TRUCK_CHANNEL_wear_cabin = ScsChannel('truck.wear.cabin', SCS_VALUE_TYPE_float)
SCS_TELEMETRY_TRUCK_CHANNEL_wear_chassis = ScsChannel('truck.wear.chassis', SCS_VALUE_TYPE_float)
SCS_TELEMETRY_TRUCK_CHANNEL_wear_engine = ScsChannel('truck.wear.engine', SCS_VALUE_TYPE_float)
SCS_TELEMETRY_TRUCK_CHANNEL_wear_transmission = ScsChannel('truck.wear.transmission', SCS_VALUE_TYPE_float)
SCS_TELEMETRY_TRUCK_CHANNEL_wear_wheels = ScsChannel('truck.wear.wheels', SCS_VALUE_TYPE_float)
SCS_TELEMETRY_TRUCK_CHANNEL_wheel_lift_offset = ScsChannel('truck.wheel.lift.offset', SCS_VALUE_TYPE_float, True, SCS_TELEMETRY_wheels_count) # indexed
SCS_TELEMETRY_TRUCK_CHANNEL_wheel_lift = ScsChannel('truck.wheel.lift', SCS_VALUE_TYPE_float, True, SCS_TELEMETRY_wheels_count) # indexed
SCS_TELEMETRY_TRUCK_CHANNEL_wheel_on_ground = ScsChannel('truck.wheel.on_ground', SCS_VALUE_TYPE_bool, True, SCS_TELEMETRY_wheels_count) # indexed
SCS_TELEMETRY_TRUCK_CHANNEL_wheel_rotation = ScsChannel('truck.wheel.rotation', SCS_VALUE_TYPE_float, True, SCS_TELEMETRY_wheels_count) # indexed
SCS_TELEMETRY_TRUCK_CHANNEL_wheel_steering = ScsChannel('truck.wheel.steering', SCS_VALUE_TYPE_float, True, SCS_TELEMETRY_wheels_count) # indexed
SCS_TELEMETRY_TRUCK_CHANNEL_wheel_substance = ScsChannel('truck.wheel.substance', SCS_VALUE_TYPE_u32, True, SCS_TELEMETRY_wheels_count) # indexed
SCS_TELEMETRY_TRUCK_CHANNEL_wheel_susp_deflection = ScsChannel('truck.wheel.suspension.deflection', SCS_VALUE_TYPE_float, True, SCS_TELEMETRY_wheels_count) # indexed
SCS_TELEMETRY_TRUCK_CHANNEL_wheel_velocity = ScsChannel('truck.wheel.angular_velocity', SCS_VALUE_TYPE_float, True, SCS_TELEMETRY_wheels_count) # indexed
SCS_TELEMETRY_TRUCK_CHANNEL_wipers = ScsChannel('truck.wipers', SCS_VALUE_TYPE_bool)
SCS_TELEMETRY_TRUCK_CHANNEL_world_placement = ScsChannel('truck.world.placement', SCS_VALUE_TYPE_dplacement)

SCS_TELEMETRY_EVENT_invalid = ScsEvent(0)
SCS_TELEMETRY_EVENT_frame_start = ScsEvent(1)
SCS_TELEMETRY_EVENT_frame_end = ScsEvent(2)
SCS_TELEMETRY_EVENT_paused = ScsEvent(3)
SCS_TELEMETRY_EVENT_started = ScsEvent(4)
SCS_TELEMETRY_EVENT_configuration = ScsEvent(5)
SCS_TELEMETRY_EVENT_gameplay = ScsEvent(6)

# Config event ids
SCS_TELEMETRY_CONFIG_controls = 'controls'
SCS_TELEMETRY_CONFIG_hshifter = 'hshifter'
SCS_TELEMETRY_CONFIG_job = 'job'
SCS_TELEMETRY_CONFIG_substances = 'substances'
SCS_TELEMETRY_CONFIG_trailer = 'trailer'
SCS_TELEMETRY_CONFIG_truck = 'truck'

# Config event attributes

# truck
SCS_TELEMETRY_CONFIG_ATTRIBUTE_brand_id = ScsAttribute('brand_id')
SCS_TELEMETRY_CONFIG_ATTRIBUTE_brand = ScsAttribute('brand')
SCS_TELEMETRY_CONFIG_ATTRIBUTE_id = ScsAttribute('id')
SCS_TELEMETRY_CONFIG_ATTRIBUTE_cargo_accessory_id = ScsAttribute('cargo.accessory.id')
SCS_TELEMETRY_CONFIG_ATTRIBUTE_chain_type = ScsAttribute('chain.type')
SCS_TELEMETRY_CONFIG_ATTRIBUTE_body_type = ScsAttribute('body.type')
SCS_TELEMETRY_CONFIG_ATTRIBUTE_license_plate = ScsAttribute('license.plate')
SCS_TELEMETRY_CONFIG_ATTRIBUTE_license_plate_country_id = ScsAttribute('license.plate.country.id')
SCS_TELEMETRY_CONFIG_ATTRIBUTE_license_plate_country = ScsAttribute('license.plate.country')
SCS_TELEMETRY_CONFIG_ATTRIBUTE_name = ScsAttribute('name')
SCS_TELEMETRY_CONFIG_ATTRIBUTE_fuel_capacity = ScsAttribute('fuel.capacity')
SCS_TELEMETRY_CONFIG_ATTRIBUTE_fuel_warning_factor = ScsAttribute('fuel.warning.factor')
SCS_TELEMETRY_CONFIG_ATTRIBUTE_adblue_capacity = ScsAttribute('adblue.capacity')
SCS_TELEMETRY_CONFIG_ATTRIBUTE_adblue_warning_factor = ScsAttribute('adblue.warning.factor')
SCS_TELEMETRY_CONFIG_ATTRIBUTE_air_pressure_warning = ScsAttribute('brake.air.pressure.warning')
SCS_TELEMETRY_CONFIG_ATTRIBUTE_air_pressure_emergency = ScsAttribute('brake.air.pressure.emergency')
SCS_TELEMETRY_CONFIG_ATTRIBUTE_oil_pressure_warning = ScsAttribute('oil.pressure.warning')
SCS_TELEMETRY_CONFIG_ATTRIBUTE_water_temperature_warning = ScsAttribute('water.temperature.warning')
SCS_TELEMETRY_CONFIG_ATTRIBUTE_battery_voltage_warning = ScsAttribute('battery.voltage.warning')
SCS_TELEMETRY_CONFIG_ATTRIBUTE_rpm_limit = ScsAttribute('rpm.limit')
SCS_TELEMETRY_CONFIG_ATTRIBUTE_forward_gear_count = ScsAttribute('gears.forward')
SCS_TELEMETRY_CONFIG_ATTRIBUTE_reverse_gear_count = ScsAttribute('gears.reverse')
SCS_TELEMETRY_CONFIG_ATTRIBUTE_differential_ratio = ScsAttribute('differential.ratio')
SCS_TELEMETRY_CONFIG_ATTRIBUTE_retarder_step_count = ScsAttribute('retarder.steps')
SCS_TELEMETRY_CONFIG_ATTRIBUTE_forward_ratio = ScsAttribute('forward.ratio', True) # indexed
SCS_TELEMETRY_CONFIG_ATTRIBUTE_reverse_ratio = ScsAttribute('reverse.ratio', True) # indexed
SCS_TELEMETRY_CONFIG_ATTRIBUTE_cabin_position = ScsAttribute('cabin.position')
SCS_TELEMETRY_CONFIG_ATTRIBUTE_head_position = ScsAttribute('head.position')
SCS_TELEMETRY_CONFIG_ATTRIBUTE_hook_position = ScsAttribute('hook.position')
SCS_TELEMETRY_CONFIG_ATTRIBUTE_wheel_count = ScsAttribute('wheels.count')
SCS_TELEMETRY_CONFIG_ATTRIBUTE_wheel_position = ScsAttribute('wheel.position', True) # indexed
SCS_TELEMETRY_CONFIG_ATTRIBUTE_wheel_steerable = ScsAttribute('wheel.steerable', True) # indexed
SCS_TELEMETRY_CONFIG_ATTRIBUTE_wheel_simulated = ScsAttribute('wheel.simulated', True) # indexed
SCS_TELEMETRY_CONFIG_ATTRIBUTE_wheel_radius = ScsAttribute('wheel.radius', True) # indexed
SCS_TELEMETRY_CONFIG_ATTRIBUTE_wheel_powered = ScsAttribute('wheel.powered', True) # indexed
SCS_TELEMETRY_CONFIG_ATTRIBUTE_wheel_liftable = ScsAttribute('wheel.liftable', True) # indexed

# hshifter
SCS_TELEMETRY_CONFIG_ATTRIBUTE_selector_count = ScsAttribute('selector.count')
SCS_TELEMETRY_CONFIG_ATTRIBUTE_slot_gear = ScsAttribute('slot.gear', True) # indexed
SCS_TELEMETRY_CONFIG_ATTRIBUTE_slot_handle_position = ScsAttribute('slot.handle.position', True) # indexed
SCS_TELEMETRY_CONFIG_ATTRIBUTE_slot_selectors = ScsAttribute('slot.selectors', True) # indexed

# controls
SCS_TELEMETRY_CONFIG_ATTRIBUTE_shifter_type = ScsAttribute('shifter.type')

SCS_SHIFTER_TYPE_arcade = 'arcade'
SCS_SHIFTER_TYPE_automatic = 'automatic'
SCS_SHIFTER_TYPE_manual = 'manual'
SCS_SHIFTER_TYPE_hshifter = 'hshifter'

# job
SCS_TELEMETRY_CONFIG_ATTRIBUTE_cargo_id = ScsAttribute('cargo.id')
SCS_TELEMETRY_CONFIG_ATTRIBUTE_cargo = ScsAttribute('cargo')
SCS_TELEMETRY_CONFIG_ATTRIBUTE_cargo_mass = ScsAttribute('cargo.mass')
SCS_TELEMETRY_CONFIG_ATTRIBUTE_cargo_unit_mass = ScsAttribute('cargo.unit.mass')
SCS_TELEMETRY_CONFIG_ATTRIBUTE_cargo_unit_count = ScsAttribute('cargo.unit.count')
SCS_TELEMETRY_CONFIG_ATTRIBUTE_destination_city_id = ScsAttribute('destination.city.id')
SCS_TELEMETRY_CONFIG_ATTRIBUTE_destination_city = ScsAttribute('destination.city')
SCS_TELEMETRY_CONFIG_ATTRIBUTE_destination_company_id = ScsAttribute('destination.company.id')
SCS_TELEMETRY_CONFIG_ATTRIBUTE_destination_company = ScsAttribute('destination.company')
SCS_TELEMETRY_CONFIG_ATTRIBUTE_source_city_id = ScsAttribute('source.city.id')
SCS_TELEMETRY_CONFIG_ATTRIBUTE_source_city = ScsAttribute('source.city')
SCS_TELEMETRY_CONFIG_ATTRIBUTE_source_company_id = ScsAttribute('source.company.id')
SCS_TELEMETRY_CONFIG_ATTRIBUTE_source_company = ScsAttribute('source.company')
SCS_TELEMETRY_CONFIG_ATTRIBUTE_income = ScsAttribute('income')
SCS_TELEMETRY_CONFIG_ATTRIBUTE_delivery_time = ScsAttribute('delivery.time')
SCS_TELEMETRY_CONFIG_ATTRIBUTE_planned_distance_km = ScsAttribute('planned_distance.km')
SCS_TELEMETRY_CONFIG_ATTRIBUTE_is_cargo_loaded = ScsAttribute('cargo.loaded')
SCS_TELEMETRY_CONFIG_ATTRIBUTE_job_market = ScsAttribute('job.market')
SCS_TELEMETRY_CONFIG_ATTRIBUTE_special_job = ScsAttribute('is.special.job')

SCS_TELEMETRY_GAMEPLAY_EVENT_job_cancelled = 'job.cancelled'
SCS_TELEMETRY_GAMEPLAY_EVENT_job_delivered = 'job.delivered'
SCS_TELEMETRY_GAMEPLAY_EVENT_player_fined = 'player.fined'
SCS_TELEMETRY_GAMEPLAY_EVENT_player_tollgate_paid = 'player.tollgate.paid'
SCS_TELEMETRY_GAMEPLAY_EVENT_player_use_ferry = 'player.use.ferry'
SCS_TELEMETRY_GAMEPLAY_EVENT_player_use_train = 'player.use.train'

SCS_TELEMETRY_GAMEPLAY_EVENT_ATTRIBUTE_cancel_penalty = ScsAttribute('cancel.penalty')
SCS_TELEMETRY_GAMEPLAY_EVENT_ATTRIBUTE_revenue = ScsAttribute('revenue')
SCS_TELEMETRY_GAMEPLAY_EVENT_ATTRIBUTE_earned_xp = ScsAttribute('earned.xp')
SCS_TELEMETRY_GAMEPLAY_EVENT_ATTRIBUTE_cargo_damage = ScsAttribute('cargo.damage')
SCS_TELEMETRY_GAMEPLAY_EVENT_ATTRIBUTE_distance_km = ScsAttribute('distance.km')
SCS_TELEMETRY_GAMEPLAY_EVENT_ATTRIBUTE_delivery_time = ScsAttribute('delivery.time')
SCS_TELEMETRY_GAMEPLAY_EVENT_ATTRIBUTE_auto_park_used = ScsAttribute('auto.park.used')
SCS_TELEMETRY_GAMEPLAY_EVENT_ATTRIBUTE_auto_load_used = ScsAttribute('auto.load.used')
SCS_TELEMETRY_GAMEPLAY_EVENT_ATTRIBUTE_fine_offence = ScsAttribute('fine.offence')
SCS_TELEMETRY_GAMEPLAY_EVENT_ATTRIBUTE_fine_amount = ScsAttribute('fine.amount')
SCS_TELEMETRY_GAMEPLAY_EVENT_ATTRIBUTE_pay_amount = ScsAttribute('pay.amount')
SCS_TELEMETRY_GAMEPLAY_EVENT_ATTRIBUTE_source_name = ScsAttribute('source.name')
SCS_TELEMETRY_GAMEPLAY_EVENT_ATTRIBUTE_target_name = ScsAttribute('target.name')
SCS_TELEMETRY_GAMEPLAY_EVENT_ATTRIBUTE_source_id = ScsAttribute('source.id')
SCS_TELEMETRY_GAMEPLAY_EVENT_ATTRIBUTE_target_id = ScsAttribute('target.id')
