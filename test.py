-- Insert data into practice_catalog (linked to platform)
INSERT INTO public.practice_catalog (platform_id, practice_code, practice_name)
SELECT p.platform_id, v.practice_code, v.practice_name
FROM public.platform_catalog p
JOIN (VALUES
  ('AZ','DATA','Data Engineering'),
  ('AZ','APP','Application Modernization'),
  ('AW','DATA','Data Analytics'),
  ('GC','APP','App Modernization')
) AS v(platform_code, practice_code, practice_name)
  ON p.platform_code = v.platform_code
ON CONFLICT DO NOTHING;  -- prevents duplicate insert

-- Insert data into offering_catalog (linked to practice)
INSERT INTO public.offering_catalog (practice_id, offering_code, offering_name)
SELECT pr.practice_id, v.offering_code, v.offering_name
FROM public.practice_catalog pr
JOIN public.platform_catalog p ON p.platform_id = pr.platform_id
JOIN (VALUES
  ('AZ','DATA','DLK','Delta Lake Setup'),
  ('AZ','APP','CNF','Containerization Setup'),
  ('AW','DATA','ANL','Analytics Pipeline'),
  ('GC','APP','DEP','Deployment Automation')
) AS v(platform_code, practice_code, offering_code, offering_name)
  ON p.platform_code = v.platform_code AND pr.practice_code = v.practice_code
ON CONFLICT DO NOTHING;





