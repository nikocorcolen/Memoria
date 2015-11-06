<?php

$id = $_GET["id"];

$dbconn = pg_connect("host=bri2.utalca.cl port=5432 dbname=Soilmap user=nmaturana password=nmaturana");

$result = pg_query($dbconn, "Select suelo from coordenadas where id = '".$id."'");
if (!$result) {
  echo "An error occurred.\n";
  exit;
}
$arr = pg_fetch_array($result, NULL, PGSQL_ASSOC);

echo json_encode($arr);
?>
