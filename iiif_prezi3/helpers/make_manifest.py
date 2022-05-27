from ..skeleton import Collection, Manifest
from ..loader import monkeypatch_schema


class MakeManifest:

    def make_manifest(self, **kwargs):
        """
        Creates a new Manifest, adds a Reference to it to the 
        calling Collection items and returns the newly created Manifest.
        Accepts keyword arguments to customize the resulting instance.
        """

        manifest = Manifest(**kwargs)
        reference = manifest.to_reference()
        self.add_item(reference)
        return manifest


monkeypatch_schema(Collection, MakeManifest)