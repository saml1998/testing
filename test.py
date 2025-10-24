-- ==============================================
-- STEP 3: LOAD OFFERING DATA INTO offering_catalog
-- Description:
--   This section links offerings to their corresponding practices.
--   It uses both platform_code and practice_code to identify
--   the correct practice_id for insertion.
--   Run this step LAST after loading platforms and practices.
-- ==============================================

INSERT INTO public.offering_catalog (practice_id, offering_code, offering_name)
SELECT pr.practice_id, v.offering_code, v.offering_name
FROM public.practice_catalog pr
JOIN public.platform_catalog p ON p.platform_id = pr.platform_id
JOIN (VALUES
('OPM_008', 'OPM_036', 'L3_00034', 'Health PLS Ops Managed Services'),
('OPM_008', 'OPM_038', 'L3_00120', 'Procurement & Supply Chain Managed Services'),
('OPM_002', 'OPM_009', 'L3_000010', 'GCP Deployment'),
('OPM_005', 'OPM_025', 'L3_000074', 'Finance Technology – NetSuite'),
('OPM_006', 'OPM_031', 'L3_000095', 'Sales Strategy'),
('OPM_007', 'OPM_034', 'L3_001100', 'Service Technology – Salesforce Service Cloud'),
('OPM_004', 'OPM_020', 'L3_000055', 'Value Creation & Growth Strategy (IVD)'),
('OPM_003', 'OPM_043', 'L3_000027', 'Cyber Strategy & Operations')
) AS v(platform_code, practice_code, offering_code, offering_name)
ON p.platform_code = v.platform_code AND pr.practice_code = v.practice_code
ON CONFLICT DO NOTHING;  -- Avoid duplicates














