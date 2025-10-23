SELECT 
    p.platform_name, 
    pr.practice_name
FROM public.practice_catalog pr
JOIN public.platform_catalog p 
    ON pr.platform_id = p.platform_id;






