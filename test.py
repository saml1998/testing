# ============================================
#   CATALOG APIS (platform, practice, offering)
# ============================================

@router.get("/catalog/platforms")
def get_all_platforms_from_db():
    """
    Get all platform records from database
    """
    sql = """
    SELECT platform_id, platform_name 
    FROM public.platform_catalog
    ORDER BY platform_name;
    """
    return fetch_all(sql)


@router.get("/catalog/practices")
def get_practices_by_platform(platformId: int):
    """
    Get all practices for a given platform
    """
    sql = """
    SELECT practice_id, practice_name 
    FROM public.practice_catalog
    WHERE platform_id = :platform_id
    ORDER BY practice_name;
    """
    return fetch_all(sql, {"platform_id": platformId})


@router.get("/catalog/offerings")
def get_offerings_by_practice(practiceId: int):
    """
    Get all offerings for a given practice
    """
    sql = """
    SELECT offering_id, offering_name 
    FROM public.offering_catalog
    WHERE practice_id = :practice_id
    ORDER BY offering_name;
    """
    return fetch_all(sql, {"practice_id": practiceId})










