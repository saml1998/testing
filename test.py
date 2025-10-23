-- Step 1: Create platform_catalog table
CREATE TABLE IF NOT EXISTS public.platform_catalog (
  platform_id   SERIAL PRIMARY KEY,
  platform_code VARCHAR(50)  NOT NULL UNIQUE,
  platform_name VARCHAR(200) NOT NULL
);

-- Step 2: Create practice_catalog table (linked to platform)
CREATE TABLE IF NOT EXISTS public.practice_catalog (
  practice_id    SERIAL PRIMARY KEY,
  platform_id    INT NOT NULL REFERENCES public.platform_catalog(platform_id) ON DELETE CASCADE,
  practice_code  VARCHAR(50) NOT NULL,
  practice_name  VARCHAR(200) NOT NULL,
  UNIQUE (platform_id, practice_code)
);

-- Step 3: Create offering_catalog table (linked to practice)
CREATE TABLE IF NOT EXISTS public.offering_catalog (
  offering_id    SERIAL PRIMARY KEY,
  practice_id    INT NOT NULL REFERENCES public.practice_catalog(practice_id) ON DELETE CASCADE,
  offering_code  VARCHAR(50) NOT NULL,
  offering_name  VARCHAR(200) NOT NULL,
  UNIQUE (practice_id, offering_code)
);




