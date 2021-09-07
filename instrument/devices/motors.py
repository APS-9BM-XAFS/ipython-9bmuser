"""
example motors
"""

__all__ = """
	Mono_Energy
	Mono_Theta
	Mono_Height
	Mono_Dtheta_Pitch
	Mono_Chi_Roll
	E_Mono_X
	WBS_Top
	WBS_Bottom
	WBS_Outboard
	WBS_Inboard
	Mono_MU1
	Mono_MV1
	Mono_MU2
	Mono_MV2
	Mono_MU3
	Mono_MV3
	Mono_Theta
	Xtal_Y
	Mono_X
	Flag_1
	Flag_2
	energy
	dTheta_pico
	dChi_inch_2
	Al_absorber
	Flag_3
	Flag_4
	Flag_5
	Tmir_Y1_us_ob
	Tmir_Y2_us_ib
	Tmir_Y3_ds
	Tmir_TX1
	Tmir_TX2
	Tmir_Bender
	M_Slit_Top
	M_Slit_Bottom
	M_Slit_Outboard
	M_Slit_Inboard
	Flag_6
	Smir_Y1_us
	Smir_Y2_ds
	Bsample_X
	Btable_X
	Bsample_Y
	Exafs_Flag
	Smir_Flag
	Btable_Y1_us
	Btable_Y2_ds_ib
	Btable_Y3_ds_ob
	Bslit_Outboard
	BSlit_Bottom
	Bslit_Top
	Bslit_Inboard
	broken
	BCM_m17
	BCM_m18
	BCM_m19
	BCM_m20
	BCM_m21
	BCM_m22
	BCM_m23
	BCM_m24
	C_Upstr_Y
	C_Dnstr_Inb_Y
	C_Dnstr_Outb_Y
	C_Upstr_X
	C_Dnstr_X
	C_Tbl_Z
	C_SampleH
	C_foil
	xtal_Tilt
	xtal_V
	xtal_Chi
	Rotation
	BSample_V_probe
	SampleIn_out
	sampleUp_down
	C_SampleV
	ADCSlitUp_bad
	ADCSlitDn
	ADCSlitInb
	ADCSlitOutb
	ADCSlitUp
	Cryo_SampV
	IRtableH
	IRtableV
""".split()
    # m1 m2 m3 m4
    # tth th chi phi

from ..session_logs import logger

logger.info(__file__)

from ophyd import EpicsMotor

# m1 = EpicsMotor("ioc:m1", name="m1", labels=("motor",))
Mono_Energy = EpicsMotor("9bmmono:En:Energy", name="Mono_Energy", labels=("motor",))
Mono_Theta = EpicsMotor("9bmmono:m1", name="Mono_Theta", labels=("motor",))
Mono_Height = EpicsMotor("9bmmono:m2", name="Mono_Height", labels=("motor",))
Mono_Dtheta_Pitch = EpicsMotor("9bmmono:m3", name="DMono_theta_Pitch", labels=("motor",))
Mono_Chi_Roll = EpicsMotor("9bmmono:m4", name="Mono_Chi_Roll", labels=("motor",))
E_Mono_X = EpicsMotor("9bmmono:m5", name="E_Mono_X", labels=("motor",))
WBS_Top = EpicsMotor("9bma:m1", name="WBS_Top", labels=("motor",))
WBS_Bottom = EpicsMotor("9bma:m2", name="WBS_Bottom", labels=("motor",))
WBS_Outboard = EpicsMotor("9bma:m3", name="WBS_Outboard", labels=("motor",))
WBS_Inboard = EpicsMotor("9bma:m4", name="WBS_Inboard", labels=("motor",))
Mono_MU1 = EpicsMotor("9bma:m5", name="Mono_MU1", labels=("motor",))
Mono_MV1 = EpicsMotor("9bma:m6", name="Mono_MV1", labels=("motor",))
Mono_MU2 = EpicsMotor("9bma:m7", name="Mono_MU2", labels=("motor",))
Mono_MV2 = EpicsMotor("9bma:m8", name="Mono_MV2", labels=("motor",))
Mono_MU3 = EpicsMotor("9bma:m9", name="Mono_MU3", labels=("motor",))
Mono_MV3 = EpicsMotor("9bma:m10", name="Mono_MV3", labels=("motor",))
Mono_Theta = EpicsMotor("9bma:m11", name="Mono_Theta", labels=("motor",))
Xtal_Y = EpicsMotor("9bma:m12", name="Xtal_Y", labels=("motor",))
Mono_X = EpicsMotor("9bma:m13", name="Mono_X", labels=("motor",))
Flag_1 = EpicsMotor("9bma:m14", name="Flag_1", labels=("motor",))
Flag_2 = EpicsMotor("9bma:m15", name="Flag_2", labels=("motor",))
energy = EpicsMotor("9bma:m16", name="energy", labels=("motor",))
dTheta_pico = EpicsMotor("9bma:m17", name="dTheta_pico", labels=("motor",))
dChi_inch_2 = EpicsMotor("9bma:m18", name="dChi_inch_2", labels=("motor",))
Al_absorber = EpicsMotor("9bma:m19", name="Al_absorber", labels=("motor",))
Flag_3 = EpicsMotor("9bma:m20", name="Flag_3", labels=("motor",))
Flag_4 = EpicsMotor("9bma:m21", name="Flag_4", labels=("motor",))
Flag_5 = EpicsMotor("9bma:m22", name="Flag_5", labels=("motor",))
Tmir_Y1_us_ob = EpicsMotor("9bma:m23", name="Tmir_Y1_us_ob", labels=("motor",))
Tmir_Y2_us_ib = EpicsMotor("9bma:m24", name="Tmir_Y2_us_ib", labels=("motor",))
Tmir_Y3_ds = EpicsMotor("9bma:m25", name="Tmir_Y3_ds", labels=("motor",))
Tmir_TX1 = EpicsMotor("9bma:m26", name="Tmir_TX1", labels=("motor",))
Tmir_TX2 = EpicsMotor("9bma:m27", name="Tmir_TX2", labels=("motor",))
Tmir_Bender = EpicsMotor("9bma:m28", name="Tmir_Bender", labels=("motor",))
M_Slit_Top = EpicsMotor("9bma:m29", name="M_Slit_Top", labels=("motor",))
M_Slit_Bottom = EpicsMotor("9bma:m30", name="M_Slit_Bottom", labels=("motor",))
M_Slit_Outboard = EpicsMotor("9bma:m31", name="M_Slit_Outboard", labels=("motor",))
M_Slit_Inboard = EpicsMotor("9bma:m32", name="M_Slit_Inboard", labels=("motor",))
Flag_6 = EpicsMotor("9bmb:m1", name="Flag_6", labels=("motor",))
Smir_Y1_us = EpicsMotor("9bmb:m2", name="Smir_Y1_us", labels=("motor",))
Smir_Y2_ds = EpicsMotor("9bmb:m3", name="Smir_Y2_ds", labels=("motor",))
Bsample_X = EpicsMotor("9bmb:m4", name="Bsample_X", labels=("motor",))
Btable_X = EpicsMotor("9bmb:m5", name="Btable_X", labels=("motor",))
Bsample_Y = EpicsMotor("9bmb:m6", name="Bsample_Y", labels=("motor",))
Exafs_Flag = EpicsMotor("9bmb:m7", name="Exafs_Flag", labels=("motor",))
Smir_Flag = EpicsMotor("9bmb:m8", name="Smir_Flag", labels=("motor",))
Btable_Y1_us = EpicsMotor("9bmb:m9", name="Btable_Y1_us", labels=("motor",))
Btable_Y2_ds_ib = EpicsMotor("9bmb:m10", name="Btable_Y2_ds_ib", labels=("motor",))
Btable_Y3_ds_ob = EpicsMotor("9bmb:m11", name="Btable_Y3_ds_ob", labels=("motor",))
Bslit_Outboard = EpicsMotor("9bmb:m12", name="Bslit_Outboard", labels=("motor",))
BSlit_Bottom = EpicsMotor("9bmb:m13", name="BSlit_Bottom", labels=("motor",))
Bslit_Top = EpicsMotor("9bmb:m14", name="Bslit_Top", labels=("motor",))
Bslit_Inboard = EpicsMotor("9bmb:m15", name="Bslit_Inboard", labels=("motor",))
broken = EpicsMotor("9bmb:m16", name="broken", labels=("motor",))
BCM_m17 = EpicsMotor("9bmb:m17", name="BCM_m17", labels=("motor",))
BCM_m18 = EpicsMotor("9bmb:m18", name="BCM_m18", labels=("motor",))
BCM_m19 = EpicsMotor("9bmb:m19", name="BCM_m19", labels=("motor",))
BCM_m20 = EpicsMotor("9bmb:m20", name="BCM_m20", labels=("motor",))
BCM_m21 = EpicsMotor("9bmb:m21", name="BCM_m21", labels=("motor",))
BCM_m22 = EpicsMotor("9bmb:m22", name="BCM_m22", labels=("motor",))
BCM_m23 = EpicsMotor("9bmb:m23", name="BCM_m23", labels=("motor",))
BCM_m24 = EpicsMotor("9bmb:m24", name="BCM_m24", labels=("motor",))
C_Upstr_Y = EpicsMotor("9bmc:m1", name="C_Upstr_Y", labels=("motor",))
C_Dnstr_Inb_Y = EpicsMotor("9bmc:m2", name="C_Dnstr_Inb_Y", labels=("motor",))
C_Dnstr_Outb_Y = EpicsMotor("9bmc:m3", name="C_Dnstr_Outb_Y", labels=("motor",))
C_Upstr_X = EpicsMotor("9bmc:m4", name="C_Upstr_X", labels=("motor",))
C_Dnstr_X = EpicsMotor("9bmc:m5", name="C_Dnstr_X", labels=("motor",))
C_Tbl_Z = EpicsMotor("9bmc:m6", name="C_Tbl_Z", labels=("motor",))
C_SampleH = EpicsMotor("9bmc:m7", name="C_SampleH", labels=("motor",))
C_foil = EpicsMotor("9bmc:m8", name="C_foil", labels=("motor",))
xtal_Tilt = EpicsMotor("9bmc:m9", name="xtal_Tilt", labels=("motor",))
xtal_V = EpicsMotor("9bmc:m10", name="xtal_V", labels=("motor",))
xtal_Chi = EpicsMotor("9bmc:m11", name="xtal_Chi", labels=("motor",))
Rotation = EpicsMotor("9bmc:m12", name="Rotation", labels=("motor",))
BSample_V_probe = EpicsMotor("9bmc:m13", name="BSample_V_probe", labels=("motor",))
SampleIn_out = EpicsMotor("9bmc:m14", name="SampleIn_out", labels=("motor",))
sampleUp_down = EpicsMotor("9bmc:m15", name="sampleUp_down", labels=("motor",))
C_SampleV = EpicsMotor("9bmc:m16", name="C_SampleV", labels=("motor",))
ADCSlitUp_bad = EpicsMotor("9bmc:m17", name="ADCSlitUp_bad", labels=("motor",))
ADCSlitDn = EpicsMotor("9bmc:m18", name="ADCSlitDn", labels=("motor",))
ADCSlitInb = EpicsMotor("9bmc:m19", name="ADCSlitInb", labels=("motor",))
ADCSlitOutb = EpicsMotor("9bmc:m20", name="ADCSlitOutb", labels=("motor",))
ADCSlitUp = EpicsMotor("9bmc:m21", name="ADCSlitUp", labels=("motor",))
Cryo_SampV = EpicsMotor("9bmc:m22", name="Cryo_SampV", labels=("motor",))
IRtableH = EpicsMotor("9bmc:m23", name="IRtableH", labels=("motor",))
IRtableV = EpicsMotor("9bmc:m24", name="IRtableV", labels=("motor",))

