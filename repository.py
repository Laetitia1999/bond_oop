from model import Bond
import csv
import pandas as pd
import os.path
import helpers_toml


class Repository:
    def __init__(self):
        self.config_file = "config.toml"
        full_path = os.path.join(os.path.dirname(__file__), self.config_file)
        self.config = helpers_toml.get_toml_data(full_path)

        file = self.config["input"]["file"]
        input_folder_path = self.config["input"]["folder"]
        full_path = os.path.join(os.path.dirname(__file__), input_folder_path, file)
        self.bonds = {}

        with open(full_path, "r", encoding="utf-8") as f:
            rows = csv.DictReader(f, delimiter=";")
            for row in rows:
                b = Bond(
                    row["Id Produit"],
                    int(row["Notional"]),
                    float(row["Bond Rate"].strip("%")) / 100.0,
                    row["Currency"],
                )
                self.bonds[b.isin] = b

    def get_df_bonds(self):
        data = []
        headers = ["isin", "Face value", "Rate", "Currency", "Coupon"]
        for b in self.bonds.values():
            data.append([b.isin, b.face_value, b.rate, b.currency, b.coupon()])

        df = pd.DataFrame(data, columns=headers)
        df.set_index("isin", inplace=True)

        return df
