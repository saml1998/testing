-- ==============================================
-- STEP 2: LOAD PRACTICE DATA INTO practice_catalog
-- Description:
--   This section links practices to their respective platforms.
--   It pulls the platform_id from platform_catalog
--   using a JOIN on platform_code.
--   Run this step AFTER platform_catalog is populated.
-- ==============================================

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
('OPM_004', 'OPM_020', 'Deals Strategy & Value Creation'),
('OPM_003', 'OPM_043', 'Cyber Defense & Engineering')
) AS v(platform_code, practice_code, practice_name)
ON p.platform_code = v.platform_code
ON CONFLICT DO NOTHING;  -- Avoid duplicates













