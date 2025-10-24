-- STEP 1: LOAD PLATFORM DATA
INSERT INTO public.platform_catalog (platform_code, platform_name)
VALUES
('OPM_008', 'Business & Supply Chain Operations'),
('OPM_002', 'Cloud Engineering, Data & Analytics'),
('OPM_003', 'Cyber, Data & Tech Risk'),
('OPM_045', 'Deals'),
('OPM_005', 'Digital Core Modernization'),
('OPM_006', 'Strategy'),
('OPM_007', 'Commercial & Service Excellence'),
('OPM_050', 'Risk & Regulatory'),
('OPM_055', 'Tax')
ON CONFLICT DO NOTHING;

-- STEP 2: LOAD PRACTICE DATA
INSERT INTO public.practice_catalog (platform_id, practice_code, practice_name)
SELECT p.platform_id, v.practice_code, v.practice_name
FROM public.platform_catalog p
JOIN (VALUES
  ('OPM_008', 'OPM_036', 'BSCO Managed Services'),
  ('OPM_008', 'OPM_020', 'Sector Operations'),
  ('OPM_002', 'OPM_031', 'App Modernization & Development'),
  ('OPM_005', 'OPM_025', 'Finance Solutions'),
  ('OPM_006', 'OPM_031', 'Enterprise & Functional Strategy'),
  ('OPM_007', 'OPM_034', 'Sales, Service & Marketing'),
  ('OPM_004', 'OPM_020', 'Deals Strategy & Value Creation')
) AS v(platform_code, practice_code, practice_name)
ON p.platform_code = v.platform_code
ON CONFLICT DO NOTHING;

-- STEP 3: LOAD OFFERING DATA
INSERT INTO public.offering_catalog (practice_id, offering_code, offering_name)
SELECT pr.practice_id, v.offering_code, v.offering_name
FROM public.practice_catalog pr
JOIN public.platform_catalog p ON p.platform_id = pr.platform_id
JOIN (VALUES
  ('OPM_008', 'OPM_036', 'L3 00034', 'Health PLS Ops Managed Services'),
  ('OPM_008', 'OPM_036', 'L3 000120', 'Procurement & Supply Chain Managed Services'),
  ('OPM_002', 'OPM_031', 'L3 000170', 'GCP Deployment'),
  ('OPM_003', 'OPM_031', 'L3 000072', 'Finance Technology - NetSuite'),
  ('OPM_006', 'OPM_031', 'L3 000157', 'Sales Strategy'),
  ('OPM_007', 'OPM_034', 'L3 000151', 'Service Technology - Salesforce Service Cloud'),
  ('OPM_004', 'OPM_020', 'L3 000051', 'Value Creation & Growth Strategy (IVD)')
) AS v(platform_code, practice_code, offering_code, offering_name)
ON p.platform_code = v.platform_code AND pr.practice_code = v.practice_code
ON CONFLICT DO NOTHING;

-- STEP 4: VERIFY DATA
SELECT COUNT(*) AS platform_count FROM public.platform_catalog;
SELECT COUNT(*) AS practice_count FROM public.practice_catalog;
SELECT COUNT(*) AS offering_count FROM public.offering_catalog;














