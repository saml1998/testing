-- LOAD PLATFORM DATA INTO platform_catalog
INSERT INTO public.platform_catalog (platform_code, platform_name)
VALUES
('OPM_008', 'Business & Supply Chain Operations'),
('OPM_002', 'Cloud Engineering, Data & Analytics'),
('OPM_003', 'Cyber, Data & Tech Risk'),
('OPM_004', 'Deals'),
('OPM_005', 'Digital Core Modernization'),
('OPM_006', 'Strategy'),
('OPM_007', 'Commercial & Service Excellence'),
('OPM_050', 'Risk & Regulatory'),
('OPM_055', 'Tax')
ON CONFLICT DO NOTHING;

-- LOAD PRACTICE DATA INTO practice_catalog
INSERT INTO public.practice_catalog (platform_id, practice_code, practice_name)
SELECT p.platform_id, v.practice_code, v.practice_name
FROM public.platform_catalog p
JOIN (VALUES
('OPM_008', 'OPM_036', 'BSCO Managed Services'),
('OPM_008', 'OPM_038', 'Sector Operations'),
('OPM_002', 'OPM_009', 'App Modernization & Development'),
('OPM_005', 'OPM_025', 'Finance Solutions'),
('OPM_006', 'OPM_031', 'Enterprise & Functional Strategy'),
('OPM_007', 'OPM_034', 'Sales, Service & Marketing'),
('OPM_004', 'OPM_020', 'Deals Strategy & Value Creation')
) AS v(platform_code, practice_code, practice_name)
ON p.platform_code = v.platform_code
ON CONFLICT DO NOTHING;

-- LOAD OFFERING DATA INTO offering_catalog
INSERT INTO public.offering_catalog (practice_id, offering_code, offering_name)
SELECT pr.practice_id, v.offering_code, v.offering_name
FROM public.practice_catalog pr
JOIN public.platform_catalog p ON p.platform_id = pr.platform_id
JOIN (VALUES
('OPM_008', 'OPM_036', 'L3_00034', 'Health PLS Ops Managed Services'),
('OPM_008', 'OPM_038', 'L3_00120', 'Procurement & Supply Chain Managed Services'),
('OPM_002', 'OPM_009', 'L3_00010', 'GCP Deployment'),
('OPM_005', 'OPM_025', 'L3_00074', 'Finance Technology - NetSuite'),
('OPM_006', 'OPM_031', 'L3_000157', 'Sales Strategy'),
('OPM_007', 'OPM_034', 'L3_001100', 'Service Technology - Salesforce Service Cloud'),
('OPM_004', 'OPM_020', 'L3_000051', 'Value Creation & Growth Strategy (IVD)')
) AS v(platform_code, practice_code, offering_code, offering_name)
ON p.platform_code = v.platform_code AND pr.practice_code = v.practice_code
ON CONFLICT DO NOTHING;

-- VERIFY DATA
SELECT * FROM public.platform_catalog;














