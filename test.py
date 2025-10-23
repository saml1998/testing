SELECT 
    p.platform_name, 
    pr.practice_name, 
    o.offering_name
FROM public.offering_catalog o
JOIN public.practice_catalog pr 
    ON o.practice_id = pr.practice_id
JOIN public.platform_catalog p 
    ON pr.platform_id = p.platform_id;







