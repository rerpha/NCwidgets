from bidict import frozenbidict

# Bidirectional map of informal component names to their NX classes
component_names = frozenbidict(
    {
        "Detector": "NXdetector",
        "Monitor": "NXmonitor",
        "Chopper": "NXdisk_chopper",
        "Source": "NXsource",
        "Slit": "NXslit",
        "Mirror": "NXmirror",
        "Monochromator": "NXmonochromator",
        "Sample": "NXsample",
        "X-ray lens": "NXxraylens",
    }
)
