from .. import Provider as AutomxotiveProvider


class Provider(AutomotiveProvider):
    """Implement automotive provider for ``pt_BR`` locale."""
    # New format since March 2017

    license_formats = ("???-####",)
