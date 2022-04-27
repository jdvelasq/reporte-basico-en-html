import os

import pandas as pd


def run():

    module_path = os.path.dirname(__file__)
    file_name = os.path.join(module_path, "../../data_lake/business/dashboard/data.csv")
    data = pd.read_csv(file_name)

    for col in data.columns:
        file_name = os.path.join(
            module_path, "../../web_servers/dashboard/figs", col + ".png"
        )
        data.plot.bar(y=col).get_figure().savefig(file_name)
        print(file_name)


if __name__ == "__main__":
    run()
