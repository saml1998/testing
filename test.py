from typing import List, Dict, Any
from app.utils.database import get_db_connection

class CatalogsADO:
    def __init__(self):
        self.db = get_db_connection()

    async def get_platforms(self) -> List[Dict[str, Any]]:
        query = """
        SELECT platform_id, platform_code, platform_name
        FROM public.platform_catalog
        ORDER BY platform_name;
        """
        rows = await self.db.execute_query(query)
        return [dict(row) for row in rows]

    async def get_practices(self, platform_id: int) -> List[Dict[str, Any]]:
        query = """
        SELECT practice_id, practice_code, practice_name
        FROM public.practice_catalog
        WHERE platform_id = $1
        ORDER BY practice_name;
        """
        rows = await self.db.execute_query(query, [platform_id])
        return [dict(row) for row in rows]

    async def get_offerings(self, practice_id: int) -> List[Dict[str, Any]]:
        query = """
        SELECT offering_id, offering_code, offering_name
        FROM public.offering_catalog
        WHERE practice_id = $1
        ORDER BY offering_name;
        """
        rows = await self.db.execute_query(query, [practice_id])
        return [dict(row) for row in rows]















