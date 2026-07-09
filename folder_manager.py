from pathlib import Path


class FolderManager:

    NO_BIDDER_SUBFOLDERS = [

        "Price Schedule for Goods",

        "Price Schedule for Related Services",

        "Discount Form",

        "Grand Summary"

    ]

    def __init__(self, root="Downloads"):

        self.root = Path(root)

        self.root.mkdir(exist_ok=True)

        self.form_folders = {}

    def create_tender_folder(self, tender_id):

        self.tender_folder = self.root / str(tender_id)

        self.tender_folder.mkdir(

            parents=True,

            exist_ok=True

        )

        print(f"\nCreated Tender Folder : {self.tender_folder}")

    def create_form_folders(self, forms):

        self.form_folders = {}

        for form in forms:

            folder = self.tender_folder / self.clean_name(form["name"])

            folder.mkdir(

                parents=True,

                exist_ok=True

            )

            self.form_folders[form["name"]] = folder

            print(f"Created : {folder.name}")

    def create_tenderer_folders(self, tenderers):

        for form_name, folder in self.form_folders.items():

            if any(

                form_name.startswith(x)

                for x in self.NO_BIDDER_SUBFOLDERS

            ):

                continue

            for tenderer in tenderers:

                bidder_folder = folder / self.clean_name(tenderer)

                bidder_folder.mkdir(

                    parents=True,

                    exist_ok=True

                )

    @staticmethod
    def clean_name(text):

        text = " ".join(text.split())

        invalid = '<>:"/\\|?*'

        for c in invalid:

            text = text.replace(c, "_")

        return text.strip()
    

        # ---------------------------------------------------------
    # Return bidder folder
    # ---------------------------------------------------------

    def get_bidder_folder(

            self,

            form_name,

            bidder_name

    ):

        form_folder = self.form_folders[form_name]

        bidder = form_folder / self.clean_name(

            bidder_name

        )

        bidder.mkdir(

            parents=True,

            exist_ok=True

        )

        return bidder
    

    def get_form_folder(

            self,

            form_name

    ):

        return self.form_folders[form_name]