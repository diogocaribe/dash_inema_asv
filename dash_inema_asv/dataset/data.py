from database.repository.seia_repository import SeiaAsvRepository
from datetime import date
import pandas as pd

seia_asv_repository = SeiaAsvRepository()

seia_asv = seia_asv_repository.gdf_select_all()
seia_asv["data_portaria"] = pd.to_datetime(seia_asv["data_portaria"])

seia_asv_sem_gom = pd.DataFrame(seia_asv)


# Datas iniciais e finais do dataframe
max_date = seia_asv["data_portaria"].max()
min_date = seia_asv["data_portaria"].min()


current_year = date.today().year
year_start = date(current_year, 1, 1)
year_end = date(current_year, 12, 31)
