"""
example scaler
"""

__all__ = """
	TIMER
	I0
	It
	Iref
	If
	sc32_6
	sc32_7
	sc32_8
	sc32_9
	sc32_10
	sc32_11
	sc32_12
	sc32_13
	sc32_14
	sc32_15	
	sc32_16
""".split()

from ..session_logs import logger

logger.info(__file__)

from ophyd.scaler import ScalerCH
from ophyd import Kind

# # make an instance of the entire scaler, for general control
scaler2 = ScalerCH("9bmc:scaler2", name="scaler1", labels=["scalers", "detectors"])

# # choose just the channels with EPICS names
scaler2.select_channels()

# # examples: make shortcuts to specific channels assigned in EPICS
TIMER = scaler2.channels.chan01.s
I0 = scaler2.channels.chan02.s
It = scaler2.channels.chan03.s
Iref = scaler2.channels.chan04.s
If = scaler2.channels.chan05.s
sc32_6 = scaler2.channels.chan06.s
sc32_7 = scaler2.channels.chan07.s
sc32_8 = scaler2.channels.chan08.s
sc32_9 = scaler2.channels.chan09.s
sc32_10 = scaler2.channels.chan10.s
sc32_11 = scaler2.channels.chan11.s
sc32_12 = scaler2.channels.chan12.s
sc32_13 = scaler2.channels.chan13.s
sc32_14 = scaler2.channels.chan14.s
sc32_15 = scaler2.channels.chan15.s
sc32_16 = scaler2.channels.chan16.s


# for item in (timebase, I0, scint, diode):
#     item._ophyd_labels_ = set(["channel", "counter",])
