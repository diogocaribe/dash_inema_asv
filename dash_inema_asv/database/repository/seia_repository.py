from database.configs.connection import DBConnectionHandler
import geopandas as gpd
from database.sql.seia import seia_sql


class SeiaAsvRepository:
    """_summary_"""

    def df_select_all(self):
        """
        :param engine: SQLAlchemy database connection engine
        :param query: Query to run
        :param params: Query parameter list
        :return: DataFrame
        """
        with DBConnectionHandler() as db:
            try:
                # data = db.session.query(MonitoramentoDissolve).all()
                data = gpd.GeoDataFrame.from_postgis(
                    sql=seia_sql,
                    con=db.get_engine(),
                    geom_col='geom', crs=4674,
                    index_col=["dtc_publicacao_portaria"],
                )
                return data
            except Exception as exception:
                # db.session.rollback()
                raise exception


seia_asv_repository = SeiaAsvRepository()

seia_asv = seia_asv_repository.df_select_all()
