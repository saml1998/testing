-- In postgres DB
CREATE TABLE IF NOT EXISTS public.platform_catalog (
  platform_id   SERIAL PRIMARY KEY,
  platform_code TEXT UNIQUE NOT NULL,
  platform_name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS public.practice_catalog (
  practice_id   SERIAL PRIMARY KEY,
  platform_id   INT NOT NULL REFERENCES public.platform_catalog(platform_id) ON DELETE CASCADE,
  practice_code TEXT NOT NULL,
  practice_name TEXT NOT NULL,
  UNIQUE (platform_id, practice_code)
);

CREATE TABLE IF NOT EXISTS public.offering_catalog (
  offering_id   SERIAL PRIMARY KEY,
  practice_id   INT NOT NULL REFERENCES public.practice_catalog(practice_id) ON DELETE CASCADE,
  offering_code TEXT NOT NULL,
  offering_name TEXT NOT NULL,
  UNIQUE (practice_id, offering_code)
);














