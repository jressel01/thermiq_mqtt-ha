# ThermIQ generated register definitions
FIELD_REGNUM = 0
FIELD_REGTYPE = 1
FIELD_UNIT = 2
FIELD_MINVALUE = 3
FIELD_MAXVALUE = 4
FIELD_BITMASK = 3


# Register as sensors
reg_id = {
#  reg_id          : ['reg#' ],
  'outdoor_t'                    : ['r00', 'temperature',            'ºC',                           ],
  'indoor_t'                     : ['r01', 'temperature',            'ºC',                           ],
  'indoor_dec_t'                 : ['r02', 'temperature',            '0.1C',                          ],
  'indoor_target_t'              : ['r03', 'temperature',            'ºC',                           ],
  'indoor_target_dec_t'          : ['r04', 'temperature',            '0.1C',                          ],
  'supplyline_t'                 : ['r05', 'temperature',            'ºC',                           ],
  'returnline_t'                 : ['r06', 'temperature',            'ºC',                           ],
  'boiler_t'                     : ['r07', 'temperature',            'ºC',                           ],
  'brine_out_t'                  : ['r08', 'temperature',            'ºC',                           ],
  'brine_in_t'                   : ['r09', 'temperature',            'ºC',                           ],
  'cooling_t'                    : ['r0a', 'temperature',            'ºC',                           ],
  'supply_shunt_t'               : ['r0b', 'temperature',            'ºC',                           ],
  'current_consumed_a'           : ['r0c', 'sensor',                 'A',                             ],
  'boiler_3kw_on'                : ['r0d', 'binary_sensor',          'A',            0x0001           ],
  'boiler_6kw_on'                : ['r0d', 'binary_sensor',          'A',            0x0002           ],
  'supplyline_target_t'          : ['r0e', 'temperature',            'ºC',                           ],
  'supplyline_shunt_target_t'    : ['r0f', 'temperature',            'ºC',                           ],
  'brine_pump_on'                : ['r10', 'binary_sensor',          'ºC',          0x0001           ],
  'compressor_on'                : ['r10', 'binary_sensor',          'ºC',          0x0002           ],
  'supply_pump_on'               : ['r10', 'binary_sensor',          'ºC',          0x0004           ],
  'hotwaterproduction_on'        : ['r10', 'binary_sensor',          'ºC',          0x0008           ],
  'aux2_heating_on'              : ['r10', 'binary_sensor',          'ºC',          0x0010           ],
  'shunt1_n'                     : ['r10', 'binary_sensor',          'ºC',          0x0020           ],
  'shunt1_p'                     : ['r10', 'binary_sensor',          'ºC',          0x0040           ],
  'aux1_heating_on'              : ['r10', 'binary_sensor',          'ºC',          0x0080           ],
  'shunt2_n'                     : ['r11', 'binary_sensor',          'ºC',          0x0001           ],
  'shunt2_p'                     : ['r11', 'binary_sensor',          'ºC',          0x0002           ],
  'shount_cooling_n'             : ['r11', 'binary_sensor',          'ºC',          0x0004           ],
  'shount_cooling_p'             : ['r11', 'binary_sensor',          'ºC',          0x0008           ],
  'active_cooling_on'            : ['r11', 'binary_sensor',          'ºC',          0x0010           ],
  'passive_cooling_on'           : ['r11', 'binary_sensor',          'ºC',          0x0020           ],
  'alarm_indication_on'          : ['r11', 'binary_sensor',          'ºC',          0x0040           ],
  'pwm_out_period'               : ['r12', 'sensor',                 '%',                             ],
  'highpressure_alm'             : ['r13', 'binary_sensor',          '%',            0x0001           ],
  'lowpressure_alm'              : ['r13', 'binary_sensor',          '%',            0x0002           ],
  'motorbreaker_alm'             : ['r13', 'binary_sensor',          '%',            0x0004           ],
  'brine_flow_alm'               : ['r13', 'binary_sensor',          '%',            0x0008           ],
  'brine_temperature_alm'        : ['r13', 'binary_sensor',          '%',            0x0010           ],
  'outdoor_sensor_alm'           : ['r14', 'binary_sensor',          '%',            0x0001           ],
  'supplyline_sensor_alm'        : ['r14', 'binary_sensor',          '%',            0x0002           ],
  'returnline_sensor_alm'        : ['r14', 'binary_sensor',          '%',            0x0004           ],
  'boiler_sensor_alm'            : ['r14', 'binary_sensor',          '%',            0x0008           ],
  'indoor_sensor_alm'            : ['r14', 'binary_sensor',          '%',            0x0010           ],
  'phase_order_alm'              : ['r14', 'binary_sensor',          '%',            0x0020           ],
  'overheating_alm'              : ['r14', 'binary_sensor',          '%',            0x0040           ],
  'demand1'                      : ['r15', 'sensor',                 '',                              ],
  'demand2'                      : ['r16', 'sensor',                 '',                              ],
  'pressurepipe_t'               : ['r17', 'temperature',            'ºC',                           ],
  'hgw_water_t'                  : ['r18', 'temperature',            'ºC',                           ],
  'integral1'                    : ['r19', 'sensor',                 'Cmin',                          ],
  'integral1_a_limit'            : ['r1a', 'sensor',                 '',                              ],
  'defrost_time_m'               : ['r1b', 'time',                   '*10s',                          ],
  'time_to_start_min_m'          : ['r1c', 'time',                   'min',                           ],
  'sw_version'                   : ['r1d', 'sensor',                 '',                              ],
  'supply_pump_speed'            : ['r1e', 'sensor',                 '%',                             ],
  'brine_pump_speed'             : ['r1f', 'sensor',                 '%',                             ],
  'status3_m'                    : ['r20', 'sensor',                 '',                              ],
  'indoor_requested_t'           : ['r32', 'temperature_input',      'ºC',               0,     50   ],
  'main_mode'                    : ['r33', 'select_input',           'mode',              0,     16   ],
  'integral1_curve_slope'        : ['r34', 'temperature_input',      'ºC',               0,    200   ],
  'integral1_curve_min'          : ['r35', 'temperature_input',      'ºC',               0,    200   ],
  'integral1_curve_max'          : ['r36', 'temperature_input',      'ºC',               0,    200   ],
  'integral1_curve_p5'           : ['r37', 'temperature_input',      'ºC',               0,    200   ],
  'integral1_curve_0'            : ['r38', 'temperature_input',      'ºC',               0,    200   ],
  'integral1_curve_n5'           : ['r39', 'temperature_input',      'ºC',               0,    200   ],
  'heating_stop_t'               : ['r3a', 'temperature_input',      'ºC',               0,    200   ],
  'reduction_t'                  : ['r3b', 'temperature_input',      'ºC',               0,    100   ],
  'room_factor'                  : ['r3c', 'temperature_input',      'ºC',               0,      2   ],
  'integral2_curve_slope'        : ['r3d', 'temperature_input',      'ºC',               0,    200   ],
  'integral2_curve_min'          : ['r3e', 'temperature_input',      'ºC',               0,    200   ],
  'integral2_curve_max'          : ['r3f', 'temperature_input',      'ºC',               0,    200   ],
  'integral2_curve_target'       : ['r40', 'temperature_input',      'ºC',               0,    200   ],
  'integral2_curve_actual'       : ['r41', 'temperature_input',      'ºC',               0,    200   ],
  'outdoor_stop_t'               : ['r42', 'temperature_input',      'ºC',               0,    100   ],
  'pressure_pipe_limit_t'        : ['r43', 'temperature_input',      'ºC',               0,    200   ],
  'hotwater_start_t'             : ['r44', 'temperature_input',      'ºC',               0,    100   ],
  'hotwater_runtime_m'           : ['r45', 'time_input',             'min',               0,  32767   ],
  'heatpump_runtime_m'           : ['r46', 'time_input',             'min',               0,  32767   ],
  'legionella_runtime_m'         : ['r47', 'sensor_dygn_input',      'dygn',         -32768,  32767   ],
  'legionella_stop_t'            : ['r48', 'temperature_input',      'ºC',               0,    100   ],
  'integral1_a_limit'            : ['r49', 'sensor_input',           'Cmin',         -32768,  32767   ],
  'integral1_hysteresis_t'       : ['r4a', 'temperature_input',      'ºC',               0,    100   ],
  'returnline_max_t'             : ['r4b', 'temperature_input',      'ºC',               0,    100   ],
  'start_interval_min_m'         : ['r4c', 'time_input',             'min',               0,  32767   ],
  'brine_min_t'                  : ['r4d', 'temperature_input',      'ºC',             -25,    100   ],
  'cooling_target_t'             : ['r4e', 'temperature_input',      'ºC',               0,     50   ],
  'integral2_a_limit'            : ['r4f', 'sensor_input',           '10 Cmin',           0,    200   ],
  'integral2_hysteresis_t'       : ['r50', 'temperature_input',      'ºC',               0,    100   ],
  'elect_boiler_steps_max'       : ['r51', 'sensor_antal_input',     'antal',        -32768,  32767   ],
  'current_consumption_max_a'    : ['r52', 'sensor_input',           'A',            -32768,  32767   ],
  'shunt_time_s'                 : ['r53', 'time_input',             's',                 0,  32767   ],
  'hotwater_stop_t'              : ['r54', 'temperature_input',      'ºC',               0,    100   ],
  'manual_test_mode_on'          : ['r55', 'select',                 'mode',                          ],
  'status7'                      : ['r56', 'sensor',                 '',                              ],
  'language'                     : ['r57', 'sensor_spr㤫',          'språk',                        ],
  'status8'                      : ['r58', 'sensor',                 '',                              ],
  'factory_reset_req'            : ['r59', 'sensor_inst',            'inst',                          ],
  'runtime_counters_reset_req'   : ['r5a', 'sensor_boolsk',          'Boolsk',                        ],
  'outdoor_sensor_offset_t'      : ['r5b', 'temperature',            'ºC',                           ],
  'supplyline_sensor_offset_t'   : ['r5c', 'temperature',            'ºC',                           ],
  'returnline_sensor_offset_t'   : ['r5d', 'temperature',            'ºC',                           ],
  'boiler_sensor_offset_t'       : ['r5e', 'temperature',            'ºC',                           ],
  'brine_in_sensor_offset_t'     : ['r5f', 'temperature',            'ºC',                           ],
  'brine_out_sensor_offset_t'    : ['r60', 'temperature',            'ºC',                           ],
  'heatingsystem_type'           : ['r61', 'sensor_typ',             'typ',                           ],
  'opt_phasemeassure_installed'  : ['r62', 'binary_sensor',          'typ',          0x0001           ],
  'opt_2_installed'              : ['r62', 'binary_sensor',          'typ',          0x0002           ],
  'opt_hgw_installed'            : ['r62', 'binary_sensor',          'typ',          0x0004           ],
  'opt_4_installed'              : ['r62', 'binary_sensor',          'typ',          0x0008           ],
  'opt_5_installed'              : ['r62', 'binary_sensor',          'typ',          0x0010           ],
  'opt_6_installed'              : ['r62', 'binary_sensor',          'typ',          0x0020           ],
  'opt_optimum_installed'        : ['r62', 'binary_sensor',          'typ',          0x0040           ],
  'opt_flowguard_installed'      : ['r62', 'binary_sensor',          'typ',          0x0080           ],
  'internal_logging_t'           : ['r63', 'time',                   'min',                           ],
  'brine_runout_t'               : ['r64', 'time',                   '*10s',                          ],
  'brine_run_in'                 : ['r65', 'time',                   '*10s',                          ],
  'legionella_run_on'            : ['r66', 'sensor_boolsk',          'Boolsk',                        ],
  'legionell_run_length_h'       : ['r67', 'time',                   'h',                             ],
  'compressor_runtime_h'         : ['r68', 'time',                   'h',                             ],
  'msd1_dvp'                     : ['r69', 'sensor',                 '',                              ],
  'boiler_3kw_runtime_h'         : ['r6a', 'time',                   'h',                             ],
  'msd1_dtp'                     : ['r6b', 'sensor',                 '',                              ],
  'hotwater_runtime_h'           : ['r6c', 'time',                   'h',                             ],
  'msd1_dvv'                     : ['r6d', 'sensor',                 '',                              ],
  'passive_cooling_runtime_h'    : ['r6e', 'time',                   'h',                             ],
  'msd1_d'                       : ['r6f', 'sensor',                 '',                              ],
  'active_cooling_runtime_h'     : ['r70', 'time',                   'h',                             ],
  'msd1_d'                       : ['r71', 'sensor',                 '',                              ],
  'boiler_6kw_on_runtime_h'      : ['r72', 'time',                   'h',                             ],
  'msd1_d'                       : ['r73', 'sensor',                 '',                              ],
  'graph_display_offset'         : ['r74', 'sensor',                 '',                              ],
  'room_sensor_set_t'            : ['rf0', 'temperature_input',      'ºC',               0,     50   ],
  'time'                         : ['rf1', 'time',                   's',                 0,     50   ],

}

# Translation dictionary
id_names = {  
  'outdoor_t'                    : ['Outdoor temp.', 'Utomhustemp.', 'Ulkolämpötila', 'Utendørstemp.', 'Außentemperatur'],
  'indoor_t'                     : ['Indoor temp.', 'Rumstemp. är', 'Huonelämpötila on', 'Romstemp. er', 'Innentemperatur, Ist'],
  'indoor_dec_t'                 : ['Indoor temp., decimal', 'Rumstemp. är, decimal', 'Huonelämp. on, decimal', 'Romstemp. er, desimal', 'Innentemp., Ist, decimal'],
  'indoor_target_t'              : ['Indoor target temp.', 'Rumstemp. bör', 'Huonelämpötila oleva', 'Romstemp. bør', 'Innentemperatur, Soll'],
  'indoor_target_dec_t'          : ['Indoor target temp., decimal', 'Rumstemp. bör, decimal', 'Huonelämpötila oleva, decimal', 'Romstemp. bør, desimal', 'Innentemp., Soll, decimal'],
  'supplyline_t'                 : ['Supplyline temp.', 'Framledningstemp.', 'Menovesi lämpötila', 'Turtemp.', 'Vorlauftemperatur'],
  'returnline_t'                 : ['Returnline temp.', 'Returledningstemp.', 'Paluuvesi lämpötila', 'Returtemp.', 'Rücklauftemperatur'],
  'boiler_t'                     : ['Hotwater temp.', 'Varmvattentemp.', 'Lämminvesilämpötila', 'Varmtvannstemp.', 'Warmwassertemperatur'],
  'brine_out_t'                  : ['Brine out temp.', 'Brine ut temp.', 'Keruu meno lämpötila', 'Brine ut temp.', 'Soleablasstemperatur'],
  'brine_in_t'                   : ['Brine in temp.', 'Brine in temp.', 'Keruu tulo lämpötila', 'Brine inn temp.', 'Soleeinlasstemperatur'],
  'cooling_t'                    : ['Cooling temp.', 'Kylning temp.', 'Jäähdytys lämpötila', 'Kjølings temp.', 'Kühlung Temperatur'],
  'supply_shunt_t'               : ['Supplyline temp., shunt', 'Framledn.temp., shunt', 'Menovesi lämpötila, shuntti', 'Tur temp., shunt', 'Vorlauftemperatur, Mischer'],
  'current_consumed_a'           : ['Electrical Current', 'Strömförbrukning', 'Virran kulutus', 'Strømforbruk', 'Stromverbrauch'],
  'boiler_3kw_on'                : ['Aux. heater 3 kW', 'Tillsats 3 kW', 'Lisälämpö 3 kW', 'Tilskudd 3 kW', 'Elektrozusatz 3 kW'],
  'boiler_6kw_on'                : ['Aux. heater 6 kW', 'Tillsats 6 kW', 'Lisälämpö 6 kW', 'Tilskudd 6 kW', 'Elektrozusatz 6 kW'],
  'supplyline_target_t'          : ['Supplyline target temp.', 'Framledningstemp., bör', 'Meno lämpötila, oleva', 'Turtemp., bør', 'Vorlauftemperatur, Soll'],
  'supplyline_shunt_target_t'    : ['Supplyline target temp., shunt', 'Framledn.temp., shunt, bör', 'Meno lämpötila, shuntti, oleva', 'Tur temp., shunt, bør', 'Vorlauftemp., Mischer, Soll'],
  'brine_pump_on'                : ['Brinepump', 'Brinepump', 'Keruupumppu', 'Brinepumpe', 'Solepumpe'],
  'compressor_on'                : ['Compressor', 'Kompressor', 'Kompressori', 'Kompressor', 'Kompressor'],
  'supply_pump_on'               : ['Flowlinepump', 'Cirkulationspump', 'Kiertopumppu', 'Sirkulasjonspumpe', 'Umwälzpumpe'],
  'hotwaterproduction_on'        : ['Hotwater production.', 'Varmvattenprod.', 'Lämminvesituotanto', 'Varmtvannsprod.', 'Warmwasserbereitung'],
  'aux2_heating_on'              : ['Auxilliary 2', 'Tillsats 2', 'Lisälämpö 2', 'Tilskudd 2', 'Zusatzheizung 2'],
  'shunt1_n'                     : ['Shunt -', 'Shunt -', 'Shuntti-', 'Shunt -', 'Mischer -'],
  'shunt1_p'                     : ['Shunt +', 'Shunt +', 'Shuntti+', 'Shunt +', 'Mischer +'],
  'aux1_heating_on'              : ['Auxilliary 1', 'Tillsats 1', 'Lisälämpö 1', 'Tilskudd 1', 'Zusatzheizung 1'],
  'shunt2_n'                     : ['Shuntgroup -', 'Shuntgrupp -', 'Shunttiryhmä -', 'Shuntgruppe -', 'Mischergruppe -'],
  'shunt2_p'                     : ['Shuntgroup +', 'Shuntgrupp +', 'Shunttiryhmä +', 'Shuntgruppe +', 'Mischergruppe +'],
  'shount_cooling_n'             : ['Shunt cooling -', 'Shunt kylning -', 'Shuntin jäähdytys -', 'Shunt kjøling -', 'Mischer Kühlung -'],
  'shount_cooling_p'             : ['Shunt cooling +', 'Shunt kylning +', 'Shuntin jäähdytys +', 'Shunt kjøling +', 'Mischer Kühlung +'],
  'active_cooling_on'            : ['Active cooling', 'Aktiv kyla', 'Aktiivinen jäähdytys', 'Aktiv kjøling', 'Aktive Kühlung'],
  'passive_cooling_on'           : ['Passive cooling', 'Passiv kyla', 'Passiivinen jäähdytys', 'Passiv kjøling', 'Passive Külung'],
  'alarm_indication_on'          : ['Alarm', 'Larm', 'Hälytys', 'Alarm', 'Alarm'],
  'pwm_out_period'               : ['PWM Out', 'PWM Out', 'PWM Out', 'PWM Out', 'PWM Out'],
  'highpressure_alm'             : ['Alarm highpr.pressostate', 'Larm högtr.pressostat', 'Hälytys korkeapainesäädin', 'Alarmhøytr.pressostat', 'Alarm Hochdruckpressostat'],
  'lowpressure_alm'              : ['Alarm lowpr.pressostate', 'Larm lågtr.pressostat', 'Hälytys matalapainesäädin', 'Alarmlavtr.pressostat', 'Alarm Niedrigdruckpressostat'],
  'motorbreaker_alm'             : ['Alarm motorcircuit breaker', 'Larm motorskydd', 'Hälytys moottorisuoja', 'Alarmmotorvern', 'Alarm Motorschutz'],
  'brine_flow_alm'               : ['Alarm low flow brine', 'Larm lågflöde brine', 'Hälytys heikkovirtaus keruuliuos', 'Alarmlavflyt brine', 'Alarm Niedrigströmung, Sole'],
  'brine_temperature_alm'        : ['Alarm low temp. brine', 'Larm lågtemp. brine', 'Hälytys matalalämpötila keruuliuos', 'Alarmlavtemp. brine', 'Alarm Niedrigtemperatur, Sole'],
  'outdoor_sensor_alm'           : ['Alarm outdoor t-sensor', 'Larm utegivare', 'Hälytys ulkoanturi', 'Alarmutegiver', 'Alarm Außenfühler'],
  'supplyline_sensor_alm'        : ['Alarm supplyline t-sensor', 'Larm framledn.givare', 'Hälytys menoanturi', 'Alarmtur.giver', 'Alarm Vorlauffühler'],
  'returnline_sensor_alm'        : ['Alarm returnline t-sensor', 'Larm returledn.givare', 'Hälytys paluuanturi', 'Alarmretur.giver', 'Alarm Rücklauffühler'],
  'boiler_sensor_alm'            : ['Alarm hotw. t-sensor', 'Larm varmvattengivare', 'Hälytys lämminvesianturi', 'Alarmvarmtvannsgiver', 'Alarm Warmwasserfühler'],
  'indoor_sensor_alm'            : ['Alarm indoor t-sensor', 'Larm rumsgivare', 'Hälytys huoneanturi', 'Alarmromgiver', 'Alarm Innenfühler'],
  'phase_order_alm'              : ['Alarm incorrect 3-phase order', 'Larm fel fasföljd', 'Hälytys väärä faasijärjestys', 'Alarmfeilfasefølge', 'Alarm falsche Phasenfolge'],
  'overheating_alm'              : ['Alarm overheating', 'Larm överhettningsskydd', 'Hälytys ylikuumenemissuoja', 'Alarmoveropphetningsvern', 'Alarm Überhitzungsschutz'],
  'demand1'                      : ['DEMAND1', 'BEHOV1', 'TARVE1', 'BEHOV1', 'BEDARF1'],
  'demand2'                      : ['DEMAND2', 'BEHOV2', 'TARVE2', 'BEHOV2', 'BEDARF2'],
  'pressurepipe_t'               : ['Pressurepipe temp.', 'Tryckrörtemp.', 'Paineputki lämpötila', 'Trykkrørstemp.', 'Druckrohrtemperatur'],
  'hgw_water_t'                  : ['Hotw. supplyline temp.', 'Varmv.framledn.temp', 'Lämminvesi menolämpötila', 'Varmtv.Tur temp', 'Warmw.vorlauftemperatur'],
  'integral1'                    : ['Integral', 'Integral', 'Integraali', 'Integral', 'Integral'],
  'integral1_a_limit'            : ['Integral, reached A-limit', 'Integral, uppnådd A-gräns', 'Integraali, A-raja-arvo saavutettu', 'Integral, oppnådd A-grense', 'Integral, A-Grenzschritte'],
  'defrost_time_m'               : ['Defrost', 'Avfrostning', 'Defrost', 'Defrost', 'Defrost'],
  'time_to_start_min_m'          : ['Minimum time to start', 'Minimum tid till start', 'Pienin aika käynnistymiseen', 'Minimum tid til start', 'Mindestzeit bis Start'],
  'sw_version'                   : ['Program version', 'Programversion', 'Ohjelmaversio', 'Programversjon', 'Programmversion'],
  'supply_pump_speed'            : ['Flowlinepump speed', 'Cirk.pump fart', 'Kiertopumpun nopeus', 'Sirk.pump fart', 'Umwälzpumpengeschw.'],
  'brine_pump_speed'             : ['Brinepump speed', 'Brinepump fart', 'Keeruupumpun nopeus', 'Brinepumpe fart', 'Solepumpengeschw.'],
  'status3_m'                    : ['STATUS3', 'STATUS3', 'STATUS3', 'STATUS3', 'STATUS3'],
  'indoor_requested_t'           : ['Indoor target temp.', 'Rumstemp., bör', 'Huonelämpötila oleva', 'Romstemp., bør', 'Innentemperatur, Soll'],
  'main_mode'                    : ['Mode', 'Driftläge', 'Käyttötila', 'Driftsmodus', 'Betriebszustand'],
  'integral1_curve_slope'        : ['Curve', 'Kurva', 'Käyrä', 'Kurve', 'Heizkurve'],
  'integral1_curve_min'          : ['Curve min', 'Kurva min', 'Käyrä min', 'Kurve min', 'Kurve min'],
  'integral1_curve_max'          : ['Curve max', 'Kurva max', 'Käyrä max', 'Kurve maks', 'Kurve max'],
  'integral1_curve_p5'           : ['Curve +5', 'Kurva +5', 'Käyrä +5', 'Kurve +5', 'Kurve +5'],
  'integral1_curve_0'            : ['Curve 0', 'Kurva 0', 'Käyrä 0', 'Kurve 0', 'Kurve 0'],
  'integral1_curve_n5'           : ['Curve -5', 'Kurva -5', 'Käyrä -5', 'Kurve -5', 'Kurve -5'],
  'heating_stop_t'               : ['Heatstop', 'Värmestopp', 'Lämmityksen pysäytys', 'Varmestopp', 'Heizstopp'],
  'reduction_t'                  : ['Temp. reduction', 'Temp. sänkning', 'Lämpötilan alennus', 'Temp. senkning', 'Nachtabsenkung'],
  'room_factor'                  : ['Room factor', 'Rumfaktor', 'Huonekerroin', 'Romfaktor', 'Raumfaktor'],
  'integral2_curve_slope'        : ['Curve 2', 'Shunt kurva', 'Shuntin käyrä', 'Shunt Kurve', 'Mischer Kurve'],
  'integral2_curve_min'          : ['Curve 2 min', 'Shunt kurva min', 'Shuntin käyrä, min', 'Shunt Kurve min', 'Mischer Kurve min'],
  'integral2_curve_max'          : ['Curve 2 max', 'Shunt kurva max', 'Shuntin käyrä, max', 'Shunt Kurve maks', 'Mischer Kurve max'],
  'integral2_curve_target'       : ['Curve 2, Target', 'Shunt kurva, bör', 'Shuntin käyrä, oleva', 'Shunt Kurve, bør', 'Mischer Kurve, Soll'],
  'integral2_curve_actual'       : ['Curve 2, Actual', 'Shunt kurva, är', 'Shuntin käyrä, on', 'Shunt kurve, er', 'Mischer Kurve, Ist'],
  'outdoor_stop_t'               : ['Outdoor stop temp. (20=-20C)', 'Utestopp temp, (20=-20C)', 'Ulkolämpötila  pysäytys (20=-20C)', 'Ute stop temp. (20=-20C)', 'Außentemp. Stop (20=-20C)'],
  'pressure_pipe_limit_t'        : ['Pressurepipe, temp. limit', 'Tryckrör, temp.gräns', 'Paineputki, lämpöraja', 'Trykkrør, temp.grense', 'Druckrohr, Temperaturgrenze'],
  'hotwater_start_t'             : ['Hotwater starttemp.', 'Varmvatten starttemp.', 'Lämminvesi, alkulämpötila', 'Varmtvann starttemp.', 'Warmwasser, Starttemperatur'],
  'hotwater_runtime_m'           : ['Hotwater operating time', 'Varmvattentid', 'Lämminvesi aika', 'Varmtvanntid', 'Warmwasserzeit'],
  'heatpump_runtime_m'           : ['Heatpump operating time', 'Värmetid', 'Lämmitysaika', 'Varmetid', 'Heizzeit'],
  'legionella_runtime_m'         : ['Legionella interval', 'Legionella intervall', 'Legionella toiminnon väliaika', 'Legionella intervall', 'Legionella, Intervall'],
  'legionella_stop_t'            : ['Legionella stop temp.', 'Legionella stopptemp.', 'Legionella, pysäytyslämpötila', 'Legionella stopptemp.', 'Legionella, Stopptemperatur'],
  'integral1_a_limit'            : ['Integral limit A1', 'Integralgräns A1', 'Integraaliraja A1', 'Integralgrense A1', 'Integral A1'],
  'integral1_hysteresis_t'       : ['Hysteresis, heatpump', 'Hysteresgräns, värmepump', 'Hystereesiraja, lämpöpumppu', 'Hysteresegrense, varmepumpe', 'Hysterese, Wärmepumpe'],
  'returnline_max_t'             : ['Returnline temp., max limit', 'Returledningstemp., maxgräns', 'Paluuveden lämpötila, ylänraja', 'Returtemp., maksgrense', 'Rücklauftemperatur, Maxgrenze'],
  'start_interval_min_m'         : ['Minimum starting interval', 'Minimum startintervall', 'Pienin käynnistysväli', 'Minimum startintervall', 'Minimum Startintervall'],
  'brine_min_t'                  : ['Brinetemp., min limit (-15=OFFV)', 'Brinetemp., min.gräns (-15=AV)', 'Keruulämpötila, alin raja (-15 pois)', 'Brinetemp., min.grense (-15', 'Soletemperatur, Mingrenze (-15=aus)'],
  'cooling_target_t'             : ['Cooling, target', 'Kyla, bör', 'Jäähdytys , oleva', 'Kjøling, bør', 'Kühlung, Soll'],
  'integral2_a_limit'            : ['Integral limit A2', 'Integralgräns A2', 'Integraaliraja A2', 'Integralgrense A2', 'Integral A2'],
  'integral2_hysteresis_t'       : ['Hysteresis limit, aux', 'Hysteresgräns, tillsats', 'Hystereesiraja, lisälämpö', 'Hysteresegrense, Tilskudd', 'Hysterese, Zusatz'],
  'elect_boiler_steps_max'       : ['Max step, aux', 'Max steg, tillsats', 'Max. Porras, lisälämpö', 'Maks steg, Tilskudd', 'Maximum Stufen, Zusatz'],
  'current_consumption_max_a'    : ['Electrical current, max limit', 'Strömförbrukn., maxgräns', 'Virrankulutus, yläraja', 'Strømforbrukn., maksgrense', 'Stromverbrauch, Maxgrenze'],
  'shunt_time_s'                 : ['Shunt time', 'Shunttid', 'Shunttiaika', 'Shunttid', 'Mischerzeit'],
  'hotwater_stop_t'              : ['Hotwater stop temp.', 'Varmvatten stopptemp.', 'Lämminvesi pysäytyslämpötila', 'Varmtvann stopptemp.', 'Warmwasserstopptemperatur'],
  'manual_test_mode_on'          : ['Manual test mode', 'Manuell test läge', 'Käsin testaus', 'Manuell test modus', 'Manueller Test'],
  'status7'                      : ['DT_LARMOFF', 'DT_LARMOFF', 'DT_LARMOFF', 'DT_LARMOFF', 'DT_LARMOFF'],
  'language'                     : ['Language', 'Språk', 'Kieli', 'Språk', 'Sprache'],
  'status8'                      : ['SERVFAS', 'SERVFAS', 'SERVFAS', 'SERVFAS', 'SERVFAS'],
  'factory_reset_req'            : ['Factory settings', 'Fabriksinställningar', 'Tehdasasetukset', 'Fabrikks instillinger', 'Werkseinstellung'],
  'runtime_counters_reset_req'   : ['Reset runtime counters', 'Nollställ drifttider', 'Nollaa käyntiajat', 'Nullstill drifttider', 'Nullstellung Laufzeiten'],
  'outdoor_sensor_offset_t'      : ['Calibration outdoor sensor', 'Kalibrering utegivare', 'Ulkoanturin kalibrointi', 'Kalibrering utegiver', 'Kalibrierung Außenfühler'],
  'supplyline_sensor_offset_t'   : ['Calibration supplyline sensor', 'Kalibrering framledn.givare', 'Menoanturin kalibrointi', 'Kalibrering tur.giver', 'Kalibrierung Vorlauffühler'],
  'returnline_sensor_offset_t'   : ['Calibration returnline sensor', 'Kalibrering returledn.givare', 'Paluuanturin kalibrointi', 'Kalibrering retur.giver', 'Kalibrierung Rücklauffühler'],
  'boiler_sensor_offset_t'       : ['Calibration hotwater sensor', 'Kalibrering varmvattengivare', 'Lämminvesianturin kalibrointi', 'Kalibrering Varmtvanngiver', 'Kalibrierung Warmwasserfühler'],
  'brine_in_sensor_offset_t'     : ['Calibration brine out sensor', 'Kalibrering brine ut', 'Keruu menoanturin kalibrointi', 'Kalibrering brine ut', 'Kalibrierung Soleablass'],
  'brine_out_sensor_offset_t'    : ['Calibration brine in sensor', 'Kalibrering brine in', 'Keruu paluuanturin kalibrointi', 'Kalibrering Brine inn', 'Kalibrierung Soleeinlass'],
  'heatingsystem_type'           : ['Heating system type 0=VL 4=D', 'Värmesystemtyp 0=VL 4=D', 'Lämmitysjärjestelmän tyyppi 0=VL 4=D', 'Varmesystemtype 0', 'Heizsystemtyp 0=VL 4=D'],
  'opt_phasemeassure_installed'  : ['Add-on phase order measurement', 'Tillägg fasmätning', 'Faasimittauksen lisäys', 'Tillegg fasemåling', 'Ergänzung Phasenmessung'],
  'opt_2_installed'              : ['TILL2', 'TILL2', 'TILL2', 'TILL2', 'TILL2'],
  'opt_hgw_installed'            : ['Add-on HGW', 'Tillägg HGW', 'HGW lisäys', 'Tillegg HGW', 'Ergänzung HGW'],
  'opt_4_installed'              : ['TILL4', 'TILL4', 'TILL4', 'TILL4', 'TILL4'],
  'opt_5_installed'              : ['TILL5', 'TILL5', 'TILL5', 'TILL5', 'TILL5'],
  'opt_6_installed'              : ['TILL6', 'TILL6', 'TILL6', 'TILL6', 'TILL6'],
  'opt_optimum_installed'        : ['Add-on Optimum', 'Tillägg Optimum', 'Optimum lisäys', 'Tillegg Optimum', 'Ergänzung Optimum'],
  'opt_flowguard_installed'      : ['Add-on flow guard', 'Tillägg flödesvakt', 'Virtausvahdin lisäys', 'Tillegg flytvakt', 'Ergänzung Strömungswächter'],
  'internal_logging_t'           : ['Logging time', 'Loggtid', 'Lokiaika', 'Loggtid', 'Logdauer'],
  'brine_runout_t'               : ['Brine run-out duration', 'Brinetid på', 'Keruupumpun käyntiaika', 'Brinetid på', 'Solepumpe Anlaufdauer'],
  'brine_run_in'                 : ['Brine run-in duration', 'Brinetid av', 'Keruupumpun pysähdysaika', 'Brinetid av', 'Solepumpe Nachlaufdauer'],
  'legionella_run_on'            : ['Legionella peak heating enable', 'Tillåt legionella körning', 'Legionella  toiminnon käynnistys', 'Legionella topptid aktiv', 'Legionella Spitzenwärme aktiv'],
  'legionell_run_length_h'       : ['Legionella peak heating duration', 'Legionella topptid', 'Legionella toiminnon huippulämmön aika', 'Legionella topptid', 'Legionella Spitzenwärmedauer'],
  'compressor_runtime_h'         : ['Runtime compressor', 'Drifttid kompressor', 'Kompressorin käyntiaika', 'Drifttid kompressor', 'Betriebszeit Kompressor'],
  'msd1_dvp'                     : ['DVP_MSD1', 'DVP_MSD1', 'DVP_MSD1', 'DVP_MSD1', 'DVP_MSD1'],
  'boiler_3kw_runtime_h'         : ['Runtime 3 kW', 'Drifttid 3 kW', 'Käyttöaika 3 kW', 'Drifttid 3 kW', 'Betriebszeit 3 kW'],
  'msd1_dtp'                     : ['DTS_MSD1', 'DTS_MSD1', 'DTS_MSD1', 'DTS_MSD1', 'DTS_MSD1'],
  'hotwater_runtime_h'           : ['Runtime hotwater production', 'Drifttid varmv.prod. med kompr.', 'Käyttöaika lämminvesi (kompressorilla)', 'Drifttid Varmtv.prod. med kompr.', 'Betriebszeit Warmwasser'],
  'msd1_dvv'                     : ['DVV_MSD1', 'DVV_MSD1', 'DVV_MSD1', 'DVV_MSD1', 'DVV_MSD1'],
  'passive_cooling_runtime_h'    : ['Runtime passive cooling', 'Drifttid passiv kyla', 'Käyttöaika passiviseen viilennykseen', 'Drifttid passiv kjøling', 'Betriebszeit passive Kühlung'],
  'msd1_d'                       : ['DPAS_MSD1', 'DPAS_MSD1', 'DPAS_MSD1', 'DPAS_MSD1', 'DPAS_MSD1'],
  'active_cooling_runtime_h'     : ['Runtime active cooling', 'Drifttid aktiv kyla', 'Käyttöaika aktiviseen viilennykseen', 'Drifttid aktiv kjøling', 'Betriebszeit aktive Kühlung'],
  'msd1_d'                       : ['DACT_MSD1', 'DACT_MSD1', 'DACT_MSD1', 'DACT_MSD1', 'DACT_MSD1'],
  'boiler_6kw_on_runtime_h'      : ['Runtime 6 kW', 'Drifttid 6 kW', 'Käyttöaika 6 kW', 'Drifttid 6 kW', 'Betriebszeit 6 kW'],
  'msd1_d'                       : ['DTS2_MSD1', 'DTS2_MSD1', 'DTS2_MSD1', 'DTS2_MSD1', 'DTS2_MSD1'],
  'graph_display_offset'         : ['GrafCounterOffSet   ', 'GrafCounterOffSet   ', 'GrafCounterOffSet   ', 'GrafCounterOffSet   ', 'GrafCounterOffSet   '],
  'room_sensor_set_t'            : ['Room sensor, Set target','Rums sensor, Styrvärde', 'Room sensor, Set target', 'Room sensor, Set target', 'Room sensor, Set target'],

}
# Unit dictionary
id_units = {  
  'outdoor_t'                    : 'ºC',
  'indoor_t'                     : 'ºC',
  'indoor_dec_t'                 : '0.1C',
  'indoor_target_t'              : 'ºC',
  'indoor_target_dec_t'          : '0.1C',
  'supplyline_t'                 : 'ºC',
  'returnline_t'                 : 'ºC',
  'boiler_t'                     : 'ºC',
  'brine_out_t'                  : 'ºC',
  'brine_in_t'                   : 'ºC',
  'cooling_t'                    : 'ºC',
  'supply_shunt_t'               : 'ºC',
  'current_consumed_a'           : 'A',
  'boiler_3kw_on'                : 'Boolean',
  'boiler_6kw_on'                : 'Boolean',
  'supplyline_target_t'          : 'ºC',
  'supplyline_shunt_target_t'    : 'ºC',
  'brine_pump_on'                : 'Boolean',
  'compressor_on'                : 'Boolean',
  'supply_pump_on'               : 'Boolean',
  'hotwaterproduction_on'        : 'Boolean',
  'aux2_heating_on'              : 'Boolean',
  'shunt1_n'                     : 'Boolean',
  'shunt1_p'                     : 'Boolean',
  'aux1_heating_on'              : 'Boolean',
  'shunt2_n'                     : 'Boolean',
  'shunt2_p'                     : 'Boolean',
  'shount_cooling_n'             : 'Boolean',
  'shount_cooling_p'             : 'Boolean',
  'active_cooling_on'            : 'Boolean',
  'passive_cooling_on'           : 'Boolean',
  'alarm_indication_on'          : 'Boolean',
  'pwm_out_period'               : '%',
  'highpressure_alm'             : 'Boolean',
  'lowpressure_alm'              : 'Boolean',
  'motorbreaker_alm'             : 'Boolean',
  'brine_flow_alm'               : 'Boolean',
  'brine_temperature_alm'        : 'Boolean',
  'outdoor_sensor_alm'           : 'Boolean',
  'supplyline_sensor_alm'        : 'Boolean',
  'returnline_sensor_alm'        : 'Boolean',
  'boiler_sensor_alm'            : 'Boolean',
  'indoor_sensor_alm'            : 'Boolean',
  'phase_order_alm'              : 'Boolean',
  'overheating_alm'              : 'Boolean',
  'demand1'                      : '  ',
  'demand2'                      : '  ',
  'pressurepipe_t'               : 'ºC',
  'hgw_water_t'                  : 'ºC',
  'integral1'                    : 'C*min',
  'integral1_a_limit'            : '  ',
  'defrost_time_m'               : '*10s',
  'time_to_start_min_m'          : 'min',
  'sw_version'                   : '  ',
  'supply_pump_speed'            : '%',
  'brine_pump_speed'             : '%',
  'status3_m'                    : '  ',
  'indoor_requested_t'           : 'ºC',
  'main_mode'                    : 'läge #',
  'integral1_curve_slope'        : 'ºC',
  'integral1_curve_min'          : 'ºC',
  'integral1_curve_max'          : 'ºC',
  'integral1_curve_p5'           : 'ºC',
  'integral1_curve_0'            : 'ºC',
  'integral1_curve_n5'           : 'ºC',
  'heating_stop_t'               : 'ºC',
  'reduction_t'                  : 'ºC',
  'room_factor'                  : 'ºC',
  'integral2_curve_slope'        : 'ºC',
  'integral2_curve_min'          : 'ºC',
  'integral2_curve_max'          : 'ºC',
  'integral2_curve_target'       : 'ºC',
  'integral2_curve_actual'       : 'ºC',
  'outdoor_stop_t'               : 'ºC',
  'pressure_pipe_limit_t'        : 'ºC',
  'hotwater_start_t'             : 'ºC',
  'hotwater_runtime_m'           : 'min',
  'heatpump_runtime_m'           : 'min',
  'legionella_runtime_m'         : 'days',
  'legionella_stop_t'            : 'ºC',
  'integral1_a_limit'            : 'C*min',
  'integral1_hysteresis_t'       : 'ºC',
  'returnline_max_t'             : 'ºC',
  'start_interval_min_m'         : 'min',
  'brine_min_t'                  : 'ºC',
  'cooling_target_t'             : 'ºC',
  'integral2_a_limit'            : '10 C*min',
  'integral2_hysteresis_t'       : 'ºC',
  'elect_boiler_steps_max'       : '# steps',
  'current_consumption_max_a'    : 'A',
  'shunt_time_s'                 : 's',
  'hotwater_stop_t'              : 'ºC',
  'manual_test_mode_on'          : 'mode #',
  'status7'                      : '  ',
  'language'                     : 'language #',
  'status8'                      : '  ',
  'factory_reset_req'            : 'setting #',
  'runtime_counters_reset_req'   : 'Boolean',
  'outdoor_sensor_offset_t'      : 'ºC',
  'supplyline_sensor_offset_t'   : 'ºC',
  'returnline_sensor_offset_t'   : 'ºC',
  'boiler_sensor_offset_t'       : 'ºC',
  'brine_in_sensor_offset_t'     : 'ºC',
  'brine_out_sensor_offset_t'    : 'ºC',
  'heatingsystem_type'           : 'type #',
  'opt_phasemeassure_installed'  : 'Boolean',
  'opt_2_installed'              : 'Boolean',
  'opt_hgw_installed'            : 'Boolean',
  'opt_4_installed'              : 'Boolean',
  'opt_5_installed'              : 'Boolean',
  'opt_6_installed'              : 'Boolean',
  'opt_optimum_installed'        : 'Boolean',
  'opt_flowguard_installed'      : 'Boolean',
  'internal_logging_t'           : 'min',
  'brine_runout_t'               : '10 s',
  'brine_run_in'                 : '10 s',
  'legionella_run_on'            : 'Boolean',
  'legionell_run_length_h'       : 'h',
  'compressor_runtime_h'         : 'h',
  'msd1_dvp'                     : '  ',
  'boiler_3kw_runtime_h'         : 'h',
  'msd1_dtp'                     : '  ',
  'hotwater_runtime_h'           : 'h',
  'msd1_dvv'                     : '  ',
  'passive_cooling_runtime_h'    : 'h',
  'msd1_d'                       : '  ',
  'active_cooling_runtime_h'     : 'h',
  'msd1_d'                       : '  ',
  'boiler_6kw_on_runtime_h'      : 'h',
  'msd1_d'                       : '  ',
  'graph_display_offset'         : '  ',
  'room_sensor_set_t'            : 'ºC',

}
