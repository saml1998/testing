CREATE TABLE practice (
    id SERIAL PRIMARY KEY,
    practice_code VARCHAR(50) UNIQUE,
    practice_name VARCHAR(255),
    platform_code VARCHAR(50),
    FOREIGN KEY (platform_code) REFERENCES platform(platform_code)
);

