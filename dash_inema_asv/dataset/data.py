from database.repository.seia_repository import SeiaAsvRepository
from datetime import date

seia_asv_repository = SeiaAsvRepository()

seia_asv = seia_asv_repository.gdf_select_all()
seia_asv['dtc_prazo_validade'] = seia_asv['dtc_prazo_validade'].astype(str)

# Datas iniciais e finais do dataframe
max_date = seia_asv.index.max()
min_date = seia_asv.index.min()


current_year = date.today().year
year_start = date(current_year, 1, 1)
year_end = date(current_year, 12, 31)
