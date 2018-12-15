CREATE TABLE intron (
  snaptron_id       INT(11) NOT NULL,
  chrom             VARCHAR(20) DEFAULT NULL,
  start             INT(11)     DEFAULT NULL,
  end               INT(11)     DEFAULT NULL,
  length            INT(11)     DEFAULT NULL,
  strand            char(1) NOT NULL,
  annotated         TINYINT(1)  DEFAULT 0,
  donor             char(2)     DEFAULT NULL,
  acceptor          char(2)     DEFAULT NULL,
  left_annotated    LONGTEXT    DEFAULT "0",
  right_annotated   LONGTEXT    DEFAULT "0",
  samples           LONGTEXT    DEFAULT NULL,
  samples_count     INT(11)     DEFAULT 0,
  coverage_sum      INT(11)     DEFAULT 0,
  coverage_avg      FLOAT(11)   DEFAULT 0.0,
  coverage_median   FLOAT(11)   DEFAULT 0.0,
  source_dataset_id INT(3)      DEFAULT NULL,
  PRIMARY KEY (snaptron_id)
);
