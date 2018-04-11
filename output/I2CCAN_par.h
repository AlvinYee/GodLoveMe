typedef struct _c_DEV_ELV_Resp_10_msg_typeTag
{
	uint8 DEV_ELV_Resp_10_Data0:8;
	uint8 DEV_ELV_Resp_10_Data1:8;
	uint8 DEV_ELV_Resp_10_Data2:8;
	uint8 DEV_ELV_Resp_10_Data3:8;
	uint8 DEV_ELV_Resp_10_Data4:8;
	uint8 DEV_ELV_Resp_10_Data5:8;
	uint8 DEV_ELV_Resp_10_Data6:8;
	uint8 DEV_ELV_Resp_10_Data7:8;

}_c_DEV_ELV_Resp_10_msg_type;
typedef struct _c_DEV_ELV_Resp_09_msg_typeTag
{
	uint8 s_upload_data0:8;
	uint8 s_upload_data1:8;
	uint8 s_upload_data2:8;
	uint8 s_upload_data3:8;
	uint8 s_upload_data4:8;
	uint8 s_upload_data5:8;
	uint8 s_upload_data6:8;
	uint8 s_upload_data7:8;

}_c_DEV_ELV_Resp_09_msg_type;
typedef struct _c_DEV_ELV_Resp_08M_msg_typeTag
{
	uint8 unused0:4;
	uint8 s_tim_Multiplexer:4;
	uint8 unused1:8;
	uint8 unused2:8;
	uint8 unused3:8;
	uint8 unused4:8;
	uint8 unused5:8;
	uint8 unused6:8;
	uint8 unused7:8;

}_c_DEV_ELV_Resp_08M_msg_type;
typedef struct _c_DEV_ELV_Resp_08m3_msg_typeTag
{
	uint8 s_tim_ISR_OS_SYS0:4;
	uint8 s_tim_Multiplexer:4;
	uint8 s_tim_ISR_OS_SYS1:8;
	uint8 s_tim_ZSM_ts_20ms0:5;
	uint8 s_tim_ISR_OS_SYS2:3;
	uint8 s_tim_ZSM_ts_20ms1:8;
	uint8 s_tim_ZSM_ts_50ms0:6;
	uint8 s_tim_ZSM_ts_20ms2:2;
	uint8 s_tim_ZSM_ts_50ms1:8;
	uint8 s_tim_ZSM_ts_100ms0:7;
	uint8 s_tim_ZSM_ts_50ms2:1;
	uint8 s_tim_ZSM_ts_100ms1:8;

}_c_DEV_ELV_Resp_08m3_msg_type;
#define b_s_tim_ISR_OS_SYS_b	((((uint16)b_s_tim_ISR_OS_SYS0_b)<<0) | (((uint16)b_s_tim_ISR_OS_SYS1_b)<<4) | (((uint16)b_s_tim_ISR_OS_SYS2_b)<<12))
#define b_s_tim_ZSM_ts_20ms_b	((((uint16)b_s_tim_ZSM_ts_20ms0_b)<<0) | (((uint16)b_s_tim_ZSM_ts_20ms1_b)<<5) | (((uint16)b_s_tim_ZSM_ts_20ms2_b)<<13))
#define b_s_tim_ZSM_ts_50ms_b	((((uint16)b_s_tim_ZSM_ts_50ms0_b)<<0) | (((uint16)b_s_tim_ZSM_ts_50ms1_b)<<6) | (((uint16)b_s_tim_ZSM_ts_50ms2_b)<<14))
#define b_s_tim_ZSM_ts_100ms_b	((((uint16)b_s_tim_ZSM_ts_100ms0_b)<<0) | (((uint16)b_s_tim_ZSM_ts_100ms1_b)<<7))
typedef struct _c_DEV_ELV_Resp_08m4_msg_typeTag
{
	uint8 s_tim_ZSM_ts_1ms0:4;
	uint8 s_tim_Multiplexer:4;
	uint8 s_tim_ZSM_ts_1ms1:8;
	uint8 s_tim_ZSM_ts_5ms0:5;
	uint8 s_tim_ZSM_ts_1ms2:3;
	uint8 s_tim_ZSM_ts_5ms1:8;
	uint8 s_tim_ZSM_ts_9ms0:6;
	uint8 s_tim_ZSM_ts_5ms2:2;
	uint8 s_tim_ZSM_ts_9ms1:8;
	uint8 s_tim_ZSM_ts_10ms0:7;
	uint8 s_tim_ZSM_ts_9ms2:1;
	uint8 s_tim_ZSM_ts_10ms1:8;

}_c_DEV_ELV_Resp_08m4_msg_type;
#define b_s_tim_ZSM_ts_1ms_b	((((uint16)b_s_tim_ZSM_ts_1ms0_b)<<0) | (((uint16)b_s_tim_ZSM_ts_1ms1_b)<<4) | (((uint16)b_s_tim_ZSM_ts_1ms2_b)<<12))
#define b_s_tim_ZSM_ts_5ms_b	((((uint16)b_s_tim_ZSM_ts_5ms0_b)<<0) | (((uint16)b_s_tim_ZSM_ts_5ms1_b)<<5) | (((uint16)b_s_tim_ZSM_ts_5ms2_b)<<13))
#define b_s_tim_ZSM_ts_9ms_b	((((uint16)b_s_tim_ZSM_ts_9ms0_b)<<0) | (((uint16)b_s_tim_ZSM_ts_9ms1_b)<<6) | (((uint16)b_s_tim_ZSM_ts_9ms2_b)<<14))
#define b_s_tim_ZSM_ts_10ms_b	((((uint16)b_s_tim_ZSM_ts_10ms0_b)<<0) | (((uint16)b_s_tim_ZSM_ts_10ms1_b)<<7))
typedef struct _c_DEV_ELV_Resp_08m1_msg_typeTag
{
	uint8 s_tim_Task_MCC0:4;
	uint8 s_tim_Multiplexer:4;
	uint8 s_tim_Task_MCC1:8;
	uint8 s_tim_Task_EEH0:5;
	uint8 s_tim_Task_MCC2:3;
	uint8 s_tim_Task_EEH1:8;
	uint8 s_tim_Task_ZSM0:6;
	uint8 s_tim_Task_EEH2:2;
	uint8 s_tim_Task_ZSM1:8;
	uint8 unused0:7;
	uint8 s_tim_Task_ZSM2:1;
	uint8 unused1:8;

}_c_DEV_ELV_Resp_08m1_msg_type;
#define b_s_tim_Task_MCC_b	((((uint16)b_s_tim_Task_MCC0_b)<<0) | (((uint16)b_s_tim_Task_MCC1_b)<<4) | (((uint16)b_s_tim_Task_MCC2_b)<<12))
#define b_s_tim_Task_EEH_b	((((uint16)b_s_tim_Task_EEH0_b)<<0) | (((uint16)b_s_tim_Task_EEH1_b)<<5) | (((uint16)b_s_tim_Task_EEH2_b)<<13))
#define b_s_tim_Task_ZSM_b	((((uint16)b_s_tim_Task_ZSM0_b)<<0) | (((uint16)b_s_tim_Task_ZSM1_b)<<6) | (((uint16)b_s_tim_Task_ZSM2_b)<<14))
typedef struct _c_DEV_ELV_Resp_08m2_msg_typeTag
{
	uint8 s_tim_ISR_CAN_TX0:4;
	uint8 s_tim_Multiplexer:4;
	uint8 s_tim_ISR_CAN_TX1:8;
	uint8 s_tim_ISR_CAN_RX0:5;
	uint8 s_tim_ISR_CAN_TX2:3;
	uint8 s_tim_ISR_CAN_RX1:8;
	uint8 s_tim_ISR_CAN_ERR0:6;
	uint8 s_tim_ISR_CAN_RX2:2;
	uint8 s_tim_ISR_CAN_ERR1:8;
	uint8 s_tim_ISR_CAN_WUP0:7;
	uint8 s_tim_ISR_CAN_ERR2:1;
	uint8 s_tim_ISR_CAN_WUP1:8;

}_c_DEV_ELV_Resp_08m2_msg_type;
#define b_s_tim_ISR_CAN_TX_b	((((uint16)b_s_tim_ISR_CAN_TX0_b)<<0) | (((uint16)b_s_tim_ISR_CAN_TX1_b)<<4) | (((uint16)b_s_tim_ISR_CAN_TX2_b)<<12))
#define b_s_tim_ISR_CAN_RX_b	((((uint16)b_s_tim_ISR_CAN_RX0_b)<<0) | (((uint16)b_s_tim_ISR_CAN_RX1_b)<<5) | (((uint16)b_s_tim_ISR_CAN_RX2_b)<<13))
#define b_s_tim_ISR_CAN_ERR_b	((((uint16)b_s_tim_ISR_CAN_ERR0_b)<<0) | (((uint16)b_s_tim_ISR_CAN_ERR1_b)<<6) | (((uint16)b_s_tim_ISR_CAN_ERR2_b)<<14))
#define b_s_tim_ISR_CAN_WUP_b	((((uint16)b_s_tim_ISR_CAN_WUP0_b)<<0) | (((uint16)b_s_tim_ISR_CAN_WUP1_b)<<7))
typedef union _u_DEV_ELV_Resp_08_msg_typeTag
{
	_c_DEV_ELV_Resp_08M_msg_type DEV_ELV_Resp_08M;
	_c_DEV_ELV_Resp_08m3_msg_type DEV_ELV_Resp_08m3;
	_c_DEV_ELV_Resp_08m4_msg_type DEV_ELV_Resp_08m4;
	_c_DEV_ELV_Resp_08m1_msg_type DEV_ELV_Resp_08m1;
	_c_DEV_ELV_Resp_08m2_msg_type DEV_ELV_Resp_08m2;

}_u_DEV_ELV_Resp_08_msg_type;
typedef struct _c_DEV_ELV_Resp_07_msg_typeTag
{
	uint8 s_eeh_data_id0:8;
	uint8 s_eeh_data_id1:8;
	uint8 unused0:8;
	uint8 unused1:8;
	uint8 unused2:8;
	uint8 unused3:8;
	uint8 unused4:8;
	uint8 unused5:8;

}_c_DEV_ELV_Resp_07_msg_type;
#define b_s_eeh_data_id_b	((((uint16)b_s_eeh_data_id0_b)<<0) | (((uint16)b_s_eeh_data_id1_b)<<8))
typedef struct _c_DEV_ELV_Resp_06_msg_typeTag
{
	uint8 s_fsh_data0:8;
	uint8 s_fsh_data1:8;
	uint8 s_fsh_data2:8;
	uint8 s_fsh_data3:8;
	uint8 unused0:8;
	uint8 unused1:8;
	uint8 unused2:8;
	uint8 unused3:8;

}_c_DEV_ELV_Resp_06_msg_type;
#define b_s_fsh_data_b	((((uint32)b_s_fsh_data0_b)<<0) | (((uint32)b_s_fsh_data1_b)<<8) | (((uint32)b_s_fsh_data2_b)<<16) | (((uint32)b_s_fsh_data3_b)<<24))
typedef struct _c_DEV_ELV_Resp_05_msg_typeTag
{
	uint8 s_imo_timeout_response:8;
	uint8 s_imo_timeout_response_fails:8;
	uint8 unused0:2;
	uint8 s_wfs_freigabe:1;
	uint8 s_wfs_auth_in_progress:1;
	uint8 s_imo_response_fails:4;
	uint8 unused1:8;
	uint8 unused2:8;
	uint8 unused3:8;
	uint8 unused4:8;
	uint8 unused5:8;

}_c_DEV_ELV_Resp_05_msg_type;
typedef struct _c_DEV_ELV_Resp_04_msg_typeTag
{
	uint8 s_eeh_reset_protocol_flags_lsb1:8;
	uint8 s_eeh_reset_protocol_flags_lsb2:8;
	uint8 s_eeh_reset_protocol_flags_lsb3:8;
	uint8 s_eeh_reset_protocol_flags_msb:8;
	uint8 s_eeh_diag_protocol_flags_lsb1:8;
	uint8 s_eeh_diag_protocol_flags_lsb2:8;
	uint8 s_eeh_diag_protocol_flags_lsb3:8;
	uint8 s_eeh_diag_protocol_flags_msb:8;

}_c_DEV_ELV_Resp_04_msg_type;
typedef struct _c_DEV_ELV_Resp_03_msg_typeTag
{
	uint8 s_sbc_reset_reason:8;
	uint8 s_sbc_wakeup_reason:8;
	uint8 s_eeh_entr_sensor_togglecntr:8;
	uint8 s_eeh_elv_entriegelungszaehler_m:8;
	uint8 s_eeh_elv_entriegelungszaehler_l:8;
	uint8 s_eeh_erasecounter_msb:8;
	uint8 s_eeh_erasecounter_lsb:8;
	uint8 s_eeh_Resetcounter:8;

}_c_DEV_ELV_Resp_03_msg_type;
typedef struct _c_DEV_ELV_Resp_02_msg_typeTag
{
	uint8 s_I2C_communication_failure:2;
	uint8 s_I2C_length_failure:1;
	uint8 s_I2C_error_sda:1;
	uint8 s_I2C_error_ram:1;
	uint8 s_I2C_error_rom:1;
	uint8 s_I2C_error_cpu:1;
	uint8 s_I2C_overflow:1;
	uint8 unused0:1;
	uint8 s_I2C_state_bcs_9:3;
	uint8 s_I2C_state_bcs_10:3;
	uint8 s_I2C_resetinfo:1;
	uint8 unused1:1;
	uint8 s_coco_supply:1;
	uint8 s_coco_reset:1;
	uint8 s_I2C_hs_lock_req:1;
	uint8 s_I2C_error_pathflags:1;
	uint8 s_I2C_cnd_haco_message:1;
	uint8 s_I2C_state_peps_2:2;
	uint8 s_motordrehzahl0:8;
	uint8 s_motordrehzahl1:8;
	uint8 unused2:8;
	uint8 unused3:8;
	uint8 unused4:8;

}_c_DEV_ELV_Resp_02_msg_type;
#define b_s_motordrehzahl_b	((((uint16)b_s_motordrehzahl0_b)<<0) | (((uint16)b_s_motordrehzahl1_b)<<8))
typedef struct _c_DEV_ELV_Resp_01_msg_typeTag
{
	uint8 s_ad_ubat:8;
	uint8 s_ad_mot:8;
	uint8 s_elv_verriegelt:1;
	uint8 s_elv_entr_c2_pio:1;
	uint8 s_elv_verr_c2_pio:1;
	uint8 s_min_fahr:1;
	uint8 s_elv_entr_komm:1;
	uint8 s_elv_verr_hw:1;
	uint8 s_elv_entr_hw:1;
	uint8 s_verr_bed:1;
	uint8 s_info_ft_offen:2;
	uint8 s_info_PowerMode_s:2;
	uint8 s_info_AuthReq:2;
	uint8 s_PowerMode_s:2;
	uint8 unused0:2;
	uint8 s_info_PowerModeValid_s:1;
	uint8 s_PowerModeValid_s:1;
	uint8 s_ft_offen:1;
	uint8 s_IGNStatus_s:1;
	uint8 s_elv_fehlermode1_aktiv:1;
	uint8 s_verriegelung_sperren:1;
	uint8 s_flow_control_state:8;
	uint8 unused1:8;
	uint8 unused2:8;

}_c_DEV_ELV_Resp_01_msg_type;
typedef struct _c_DEV_ELV_Resp_00_msg_typeTag
{
	uint8 s_verriegeln_aktiv:1;
	uint8 s_entriegeln_aktiv:1;
	uint8 s_elv_entr_pio:1;
	uint8 s_elv_verr_pio:1;
	uint8 s_eeh_elv_entr:1;
	uint8 s_elv_entr:1;
	uint8 s_elv_trigger_entriegelung_anz:1;
	uint8 s_elv_trigger_verriegelung_anz:1;
	uint8 s_brueckenfehler_zyklisch_lowsid:1;
	uint8 s_hw_highside_verriegeln:1;
	uint8 s_highside_verriegeln:1;
	uint8 s_highside_entriegeln:1;
	uint8 s_lowside_verriegeln:2;
	uint8 s_lowside_entriegeln:2;
	uint8 s_starte_motorbremse:1;
	uint8 s_motorbremse_aktiv:1;
	uint8 s_elv_trigger_verriegelung_inter:1;
	uint8 s_motor_entriegeln_anz:1;
	uint8 s_motor_entriegeln:1;
	uint8 s_ad_motorbruecke:2;
	uint8 s_brueckenfehler_zyklisch_highsi:1;
	uint8 s_VerBed_Drehzahl:1;
	uint8 s_pfad_motor_start:1;
	uint8 s_pfad_bedingungen:1;
	uint8 s_pfad_trigger:1;
	uint8 s_area_highside_ready:1;
	uint8 s_area_lowside_ready:1;
	uint8 s_wirksamkeit_highside_checken:1;
	uint8 s_wirksamkeit_lowside_checken:1;
	uint8 s_VerBed_E2E_WheelsSpeedFront:3;
	uint8 s_VerBed_E2E_IgnitionAndPowerMod:3;
	uint8 s_VerBed_Ignition:1;
	uint8 s_VerBed_PowerMode:1;
	uint8 s_VerBed_WheelRr:1;
	uint8 s_VerBed_WheelRl:1;
	uint8 s_VerBed_WheelFl:1;
	uint8 s_VerBed_WheelFr:1;
	uint8 s_VerBed_E2E_WheelsSpeedRear:3;
	uint8 s_VerBed_WheelsSpeed:1;
	uint8 s_elv_trigger_verriegelung:1;
	uint8 s_motor_verriegeln_anz:1;
	uint8 s_motor_verriegeln:1;
	uint8 s_entr_bed:1;
	uint8 s_wirksamkeitsfehler_highside:1;
	uint8 s_wirksamkeitsfehler_lowside:1;
	uint8 s_VerBed_LockInhibit:1;
	uint8 s_VerBed_Mode1:1;
	uint8 unused0:7;
	uint8 s_anzeige_lkg_bewegen:1;

}_c_DEV_ELV_Resp_00_msg_type;
typedef struct _c_DIAG_ESCL_Tx_msg_typeTag
{
	uint8 ESCL_Diag_Tx0:8;
	uint8 ESCL_Diag_Tx1:8;
	uint8 ESCL_Diag_Tx2:8;
	uint8 ESCL_Diag_Tx3:8;
	uint8 ESCL_Diag_Tx4:8;
	uint8 ESCL_Diag_Tx5:8;
	uint8 ESCL_Diag_Tx6:8;
	uint8 ESCL_Diag_Tx7:8;

}_c_DIAG_ESCL_Tx_msg_type;
#define b_ESCL_Diag_Tx_b	((((uint16)b_ESCL_Diag_Tx7_b)<<0) | (((uint16)b_ESCL_Diag_Tx6_b)<<8) | (((uint16)b_ESCL_Diag_Tx5_b)<<16) | (((uint16)b_ESCL_Diag_Tx4_b)<<24) | (((uint16)b_ESCL_Diag_Tx3_b)<<32) | (((uint16)b_ESCL_Diag_Tx2_b)<<40) | (((uint16)b_ESCL_Diag_Tx1_b)<<48) | (((uint16)b_ESCL_Diag_Tx0_b)<<56))
typedef struct _c_NM_ESCL_msg_typeTag
{
	uint8 ESCL_NodeAddress:8;
	uint8 ESCL_NMDataField0:8;
	uint8 ESCL_NMDataField1:8;
	uint8 ESCL_NMDataField2:8;
	uint8 ESCL_NMDataField3:8;
	uint8 ESCL_NMDataField4:8;
	uint8 ESCL_NMDataField5:8;
	uint8 ESCL_NMDataField6:8;

}_c_NM_ESCL_msg_type;
#define b_ESCL_NMDataField_b	((((uint16)b_ESCL_NMDataField6_b)<<0) | (((uint16)b_ESCL_NMDataField5_b)<<8) | (((uint16)b_ESCL_NMDataField4_b)<<16) | (((uint16)b_ESCL_NMDataField3_b)<<24) | (((uint16)b_ESCL_NMDataField2_b)<<32) | (((uint16)b_ESCL_NMDataField1_b)<<40) | (((uint16)b_ESCL_NMDataField0_b)<<48))
typedef struct _c_ESCL_2_msg_typeTag
{
	uint8 ESCL_SUB_ID:8;
	uint8 ESCL_AuthChallenge0:8;
	uint8 ESCL_AuthChallenge1:8;
	uint8 ESCL_AuthChallenge2:8;
	uint8 ESCL_AuthChallenge3:8;
	uint8 ESCL_AuthResult:8;
	uint8 unused0:8;
	uint8 unused1:8;

}_c_ESCL_2_msg_type;
#define b_ESCL_AuthChallenge_b	((((uint16)b_ESCL_AuthChallenge3_b)<<0) | (((uint16)b_ESCL_AuthChallenge2_b)<<8) | (((uint16)b_ESCL_AuthChallenge1_b)<<16) | (((uint16)b_ESCL_AuthChallenge0_b)<<24))
typedef struct _c_ESCL_1_msg_typeTag
{
	uint8 unused0:3;
	uint8 ESCL_PromptRotateSteerWheel:1;
	uint8 ESCL_WarnFunctional:1;
	uint8 ESCL_WarnSafety:1;
	uint8 ESCL_St:2;
	uint8 unused1:8;
	uint8 unused2:8;
	uint8 unused3:8;
	uint8 unused4:8;
	uint8 unused5:8;
	uint8 ESCL_1_MsgCounter:4;
	uint8 unused6:4;
	uint8 ESCL_1_Checksum:8;

}_c_ESCL_1_msg_type;
