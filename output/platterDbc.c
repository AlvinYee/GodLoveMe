PCS
Tester
	DIAG_Req_All_Ecu
		Func_Diag_Rx, start:7, len:64, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:0.0, unit:
	DIAG_Req_ESCL_Phys
		ESCL_Diag_Request, start:7, len:64, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:0.0, unit:
TEL
	TEL_NM_PCAN
		TEL_NMDataField, start:15, len:56, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:0.0, unit:-
		TEL_NMNodeAddress, start:7, len:8, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:255.0, unit:-
PEPS
MFS
ICM
HVSM
HVAC
HCP
FCP
BCM
ACU
WCM
SVM
PAS
VCU
	VCU_NM_PCAN
		VCU_NMDataField, start:15, len:56, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:0.0, unit:-
		VCU_NMNodeAddress, start:7, len:8, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:255.0, unit:
TGW
OBC
DCU
DCDC
BMS
TCU
SRS
SAS
PCU
GSM
ESCL
	DEV_ELV_Resp_10
		DEV_ELV_Resp_10_Data, start:0, len:64, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.84467440737096e+19, unit:
	DEV_ELV_Resp_09
		s_upload_data, start:0, len:64, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.8446744074e+19, unit:
	DEV_ELV_Resp_08
		s_tim_Multiplexer, start:0, len:4, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:15.0, unit:
		s_tim_ISR_OS_SYS, start:4, len:15, endian:1, sign:+, factor:0.005, offset:0.0, Min:0.0, Max:100.0, unit:%
		s_tim_ZSM_ts_1ms, start:4, len:15, endian:1, sign:+, factor:0.005, offset:0.0, Min:0.0, Max:100.0, unit:%
		s_tim_Task_MCC, start:4, len:15, endian:1, sign:+, factor:0.005, offset:0.0, Min:0.0, Max:100.0, unit:%
		s_tim_ISR_CAN_TX, start:4, len:15, endian:1, sign:+, factor:0.005, offset:0.0, Min:0.0, Max:100.0, unit:%
		s_tim_Task_EEH, start:19, len:15, endian:1, sign:+, factor:0.005, offset:0.0, Min:0.0, Max:100.0, unit:%
		s_tim_ISR_CAN_RX, start:19, len:15, endian:1, sign:+, factor:0.005, offset:0.0, Min:0.0, Max:100.0, unit:%
		s_tim_ZSM_ts_20ms, start:19, len:15, endian:1, sign:+, factor:0.005, offset:0.0, Min:0.0, Max:100.0, unit:%
		s_tim_ZSM_ts_5ms, start:19, len:15, endian:1, sign:+, factor:0.005, offset:0.0, Min:0.0, Max:100.0, unit:%
		s_tim_ZSM_ts_9ms, start:34, len:15, endian:1, sign:+, factor:0.005, offset:0.0, Min:0.0, Max:100.0, unit:%
		s_tim_Task_ZSM, start:34, len:15, endian:1, sign:+, factor:0.005, offset:0.0, Min:0.0, Max:100.0, unit:%
		s_tim_ISR_CAN_ERR, start:34, len:15, endian:1, sign:+, factor:0.005, offset:0.0, Min:0.0, Max:100.0, unit:%
		s_tim_ZSM_ts_50ms, start:34, len:15, endian:1, sign:+, factor:0.005, offset:0.0, Min:0.0, Max:100.0, unit:%
		s_tim_ZSM_ts_10ms, start:49, len:15, endian:1, sign:+, factor:0.005, offset:0.0, Min:0.0, Max:100.0, unit:%
		s_tim_ZSM_ts_100ms, start:49, len:15, endian:1, sign:+, factor:0.005, offset:0.0, Min:0.0, Max:100.0, unit:%
		s_tim_ISR_CAN_WUP, start:49, len:15, endian:1, sign:+, factor:0.005, offset:0.0, Min:0.0, Max:100.0, unit:%
	DEV_ELV_Resp_07
		s_eeh_data_id, start:0, len:16, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:65535.0, unit:
	DEV_ELV_Resp_06
		s_fsh_data, start:0, len:32, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:0.0, unit:
	DEV_ELV_Resp_05
		s_imo_response_fails, start:16, len:4, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:15.0, unit:
		s_imo_timeout_response_fails, start:8, len:8, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:255.0, unit:
		s_wfs_auth_in_progress, start:20, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_wfs_freigabe, start:21, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_imo_timeout_response, start:0, len:8, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:255.0, unit:
	DEV_ELV_Resp_04
		s_eeh_reset_protocol_flags_lsb1, start:0, len:8, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:255.0, unit:
		s_eeh_reset_protocol_flags_lsb2, start:8, len:8, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:255.0, unit:
		s_eeh_reset_protocol_flags_lsb3, start:16, len:8, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:255.0, unit:
		s_eeh_reset_protocol_flags_msb, start:24, len:8, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:255.0, unit:
		s_eeh_diag_protocol_flags_lsb1, start:32, len:8, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:255.0, unit:
		s_eeh_diag_protocol_flags_lsb2, start:40, len:8, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:255.0, unit:
		s_eeh_diag_protocol_flags_lsb3, start:48, len:8, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:255.0, unit:
		s_eeh_diag_protocol_flags_msb, start:56, len:8, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:255.0, unit:
	DEV_ELV_Resp_03
		s_sbc_reset_reason, start:0, len:8, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:255.0, unit:
		s_sbc_wakeup_reason, start:8, len:8, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:255.0, unit:
		s_eeh_entr_sensor_togglecntr, start:16, len:8, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:255.0, unit:
		s_eeh_elv_entriegelungszaehler_m, start:24, len:8, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:255.0, unit:
		s_eeh_elv_entriegelungszaehler_l, start:32, len:8, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:255.0, unit:
		s_eeh_erasecounter_msb, start:40, len:8, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:255.0, unit:
		s_eeh_erasecounter_lsb, start:48, len:8, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:255.0, unit:
		s_eeh_Resetcounter, start:56, len:8, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:255.0, unit:
	DEV_ELV_Resp_02
		s_motordrehzahl, start:24, len:16, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:65535.0, unit:
		s_I2C_state_peps_2, start:16, len:2, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:3.0, unit:
		s_I2C_overflow, start:0, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_I2C_error_cpu, start:1, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_I2C_error_rom, start:2, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_I2C_error_ram, start:3, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_I2C_error_sda, start:4, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_I2C_length_failure, start:5, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_I2C_communication_failure, start:6, len:2, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:3.0, unit:
		s_I2C_resetinfo, start:8, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_I2C_state_bcs_10, start:9, len:3, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:7.0, unit:
		s_I2C_cnd_haco_message, start:18, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_I2C_error_pathflags, start:19, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_I2C_state_bcs_9, start:12, len:3, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:7.0, unit:
		s_I2C_hs_lock_req, start:20, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_coco_reset, start:21, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_coco_supply, start:22, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
	DEV_ELV_Resp_01
		s_PowerModeValid_s, start:36, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_info_PowerModeValid_s, start:37, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_ft_offen, start:35, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_IGNStatus_s, start:34, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_ad_ubat, start:0, len:8, endian:1, sign:+, factor:0.028846153846, offset:0.0, Min:0.0, Max:29.509615385, unit:V
		s_ad_mot, start:8, len:8, endian:1, sign:+, factor:0.028846153846, offset:0.0, Min:0.0, Max:29.5096153853, unit:V
		s_verr_bed, start:16, len:1, endian:1, sign:-, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_elv_entr_hw, start:17, len:1, endian:1, sign:-, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_elv_verr_hw, start:18, len:1, endian:1, sign:-, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_elv_entr_komm, start:19, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_min_fahr, start:20, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_elv_verr_c2_pio, start:21, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_elv_entr_c2_pio, start:22, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_PowerMode_s, start:24, len:2, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:3.0, unit:
		s_elv_verriegelt, start:23, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_info_AuthReq, start:26, len:2, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:3.0, unit:
		s_info_PowerMode_s, start:28, len:2, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:3.0, unit:
		s_info_ft_offen, start:30, len:2, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:3.0, unit:
		s_verriegelung_sperren, start:32, len:1, endian:1, sign:-, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_elv_fehlermode1_aktiv, start:33, len:1, endian:1, sign:-, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_flow_control_state, start:40, len:8, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:0.0, unit:
	DEV_ELV_Resp_00
		s_anzeige_lkg_bewegen, start:56, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_elv_trigger_verriegelung, start:55, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_motor_verriegeln_anz, start:54, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_motor_entriegeln, start:19, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_elv_trigger_verriegelung_anz, start:0, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_elv_trigger_entriegelung_anz, start:1, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_elv_entr, start:2, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_eeh_elv_entr, start:3, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_elv_verr_pio, start:4, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_elv_entr_pio, start:5, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_entriegeln_aktiv, start:6, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_verriegeln_aktiv, start:7, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_lowside_entriegeln, start:8, len:2, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:3.0, unit:
		s_lowside_verriegeln, start:10, len:2, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:3.0, unit:
		s_highside_entriegeln, start:12, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_highside_verriegeln, start:13, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_hw_highside_verriegeln, start:14, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_motor_verriegeln, start:53, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_brueckenfehler_zyklisch_lowsid, start:15, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_brueckenfehler_zyklisch_highsi, start:16, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_ad_motorbruecke, start:17, len:2, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:3.0, unit:
		s_motor_entriegeln_anz, start:20, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_elv_trigger_verriegelung_inter, start:21, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_motorbremse_aktiv, start:22, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_starte_motorbremse, start:23, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_wirksamkeit_lowside_checken, start:24, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_wirksamkeit_highside_checken, start:25, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_area_lowside_ready, start:26, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_area_highside_ready, start:27, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_pfad_trigger, start:28, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_pfad_bedingungen, start:29, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_pfad_motor_start, start:30, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_VerBed_Drehzahl, start:31, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_VerBed_LockInhibit, start:49, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_VerBed_WheelRr, start:47, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_VerBed_WheelRl, start:46, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_VerBed_WheelFl, start:45, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_VerBed_WheelFr, start:44, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_VerBed_E2E_WheelsSpeedRear, start:41, len:3, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:7.0, unit:
		s_VerBed_Mode1, start:48, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_VerBed_E2E_WheelsSpeedFront, start:37, len:3, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:7.0, unit:
		s_VerBed_WheelsSpeed, start:40, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_VerBed_E2E_IgnitionAndPowerMod, start:34, len:3, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:7.0, unit:
		s_VerBed_Ignition, start:33, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_VerBed_PowerMode, start:32, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_wirksamkeitsfehler_lowside, start:50, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_wirksamkeitsfehler_highside, start:51, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_entr_bed, start:52, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
	DIAG_ESCL_Tx
		ESCL_Diag_Tx, start:7, len:64, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:0.0, unit:
	NM_ESCL
		ESCL_NMDataField, start:15, len:56, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:0.0, unit:
		ESCL_NodeAddress, start:7, len:8, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:255.0, unit:
	ESCL_2
		ESCL_AuthResult, start:47, len:8, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:3.0, unit:
		ESCL_AuthChallenge, start:15, len:32, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:4294967295.0, unit:
		ESCL_SUB_ID, start:7, len:8, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:2.0, unit:
	ESCL_1
		ESCL_1_Checksum, start:63, len:8, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:255.0, unit:
		ESCL_1_MsgCounter, start:55, len:4, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:15.0, unit:
		ESCL_PromptRotateSteerWheel, start:4, len:1, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		ESCL_WarnFunctional, start:3, len:1, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		ESCL_WarnSafety, start:2, len:1, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		ESCL_St, start:1, len:2, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:3.0, unit:
EPS
	EPS_NM
		EPS_NMDataField, start:15, len:56, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:0.0, unit:
		EPS_NodeAddress, start:7, len:8, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:255.0, unit:
EPB
	EPB_NM
		EPB_NMDataField, start:15, len:56, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:0.0, unit:
		EPB_NodeAddress, start:7, len:8, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:255.0, unit:
EMS
	EMS_2
		EMS_EngSpdVD, start:52, len:1, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:-
		EMS_EngSpd, start:23, len:16, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:65535.0, unit:rpm
BCS
	BCS_NM
		BCS_NMDataField, start:15, len:56, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:0.0, unit:
		BCS_NodeAddress, start:7, len:8, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:255.0, unit:
	BCS_10
		BCS_10_Checksum, start:63, len:8, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:255.0, unit:
		BCS_10_MsgCounter, start:51, len:4, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:15.0, unit:
		BCS_RRWheelSpd, start:28, len:13, endian:0, sign:+, factor:0.05625, offset:0.0, Min:0.0, Max:240.0, unit:km/h
		BCS_RRWheelSpdVD, start:31, len:1, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		BCS_RLWheelSpd, start:12, len:13, endian:0, sign:+, factor:0.05625, offset:0.0, Min:0.0, Max:240.0, unit:km/h
		BCS_RLWheelSpdVD, start:5, len:1, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
	BCS_9
		BCS_9_Checksum, start:63, len:8, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:255.0, unit:
		BCS_9_MsgCounter, start:51, len:4, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:15.0, unit:
		BCS_FRWheelSpd, start:28, len:13, endian:0, sign:+, factor:0.05625, offset:0.0, Min:0.0, Max:240.0, unit:km/h
		BCS_FRWheelSpdVD, start:31, len:1, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		BCS_FLWheelSpd, start:12, len:13, endian:0, sign:+, factor:0.05625, offset:0.0, Min:0.0, Max:240.0, unit:km/h
		BCS_FLWheelSpdVD, start:5, len:1, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
ALS
GWM
	NM_GWM
		GWM_NMDataField, start:15, len:56, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:0.0, unit:
		GWM_NodeAddress, start:7, len:8, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:255.0, unit:
	PEPS_7
		PEPS_AuthResp, start:15, len:32, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:0.0, unit:
		PEPS_SUB_ID, start:7, len:8, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:2.0, unit:
	PEPS_3
		PEPS_keyComdInfor, start:15, len:8, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:255.0, unit:
		PEPS_DoorlockReq, start:4, len:1, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		PEPS_ESCLLockReq, start:30, len:1, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
	PEPS_2
		PEPS_2_Checksum, start:63, len:8, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:255.0, unit:
		PEPS_2_MsgCounter, start:55, len:4, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:15.0, unit:
		PEPS_ESCLInhabitSt, start:51, len:1, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		PEPS_IGNFbkStVD, start:46, len:1, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		PEPS_IGNFbkSt, start:45, len:1, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		PEPS_IG1RelayStVD, start:44, len:1, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		PEPS_IG1RelaySt, start:41, len:1, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		PEPS_SysPowMode_RddyVD, start:26, len:1, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		PEPS_SysPowMode_Rddy, start:25, len:2, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:3.0, unit:
	GW_BCM_2_P
		BCM_KeySt, start:9, len:2, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:3.0, unit:
		BCM_DriverDoorAjarSt, start:14, len:1, endian:0, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
Vector__XXX
	VECTOR__INDEPENDENT_SIG_MSG
		s_eeh_entr_sensor_togglecntr, start:0, len:8, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:0.0, unit:
		s_elv_verrigelung_intern, start:0, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
	DEV_ELV_Req_01
		s_upload_addr, start:0, len:32, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:4294967295.0, unit:
		s_upload_len, start:32, len:8, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:255.0, unit:
		s_upload_sig, start:40, len:24, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:16777215.0, unit:
	DEV_ELV_Req_00
		s_enable_ewi, start:0, len:8, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:255.0, unit:
		s_clear_wd_diag_data, start:16, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_clear_resetcounter, start:17, len:1, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:1.0, unit:
		s_req_fsh_counter, start:24, len:8, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:255.0, unit:
		s_tim_choice, start:32, len:4, endian:1, sign:+, factor:1.0, offset:0.0, Min:0.0, Max:0.0, unit:
