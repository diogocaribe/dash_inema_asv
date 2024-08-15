from database.configs.connection import DBConnectionHandler
import geopandas as gpd
import pandas as pd
from database.sql.seia import seia_sql_geom


class SeiaAsvRepository:
    """_summary_"""

    def gdf_select_all(self):
        """
        :param engine: SQLAlchemy database connection engine
        :param query: Query to run
        :param params: Query parameter list
        :return: DataFrame
        """
        with DBConnectionHandler() as db:
            try:
                data = gpd.GeoDataFrame.from_postgis(
                    sql=seia_sql_geom,
                    con=db.get_engine(),
                    geom_col="geom",
                    crs=4674,
                    # index_col=["gid"],
                )
                return data
            except Exception as exception:
                raise exception

    def df_select_all(self):
        """
        :param engine: SQLAlchemy database connection engine
        :param query: Query to run
        :param params: Query parameter list
        :return: DataFrame
        """
        return pd.DataFrame(self.gdf_select_all)
