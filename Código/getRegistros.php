<?php

header('Access-Control-Allow-Origin: *');

$dbconn = pg_connect("host=bri2.utalca.cl port=5432 dbname=Soilmap user=nmaturana password=nmaturana");

$result = pg_query($dbconn, "SELECT * FROM registros ORDER BY fecha DESC LIMIT 1");
if (!$result) {
  echo "An error occurred.\n";
  exit;
}
$arr = pg_fetch_array($result, NULL, PGSQL_ASSOC);

echo json_encode($arr);
?>