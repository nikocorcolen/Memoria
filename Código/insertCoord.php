
<?php /*
 * PHP PGSQL - How to insert rows into PostgreSQL table
 */
$id = $_POST["id"];
$lat = $_POST["lat"];
$lon = $_POST["lon"];

//echo $col1;
//echo $col2;
// Connecting, selecting database $dbconn = pg_connect("host=localhost
if(isset($_POST["id"]))
{
  $dbconn3 = pg_connect("host=bri2.utalca.cl port=5432 dbname=Soilmap user=nmaturana password=nmaturana");

  $selectSuelo = "SELECT domsoi FROM dsmw WHERE st_contains(geom,ST_GeomFromText('POINT(".$lon." ".$lat.")',4326))";
  $result = pg_query($dbconn3, $selectSuelo);
  $row = pg_fetch_row($result);
  $suelo = $row[0];
  var_dump($result);

  $insert = "INSERT INTO coordenadas(id, lat, lon, suelo) VALUES('".$id."', '".$lat."', '".$lon."', '".$suelo."')";
  $result = pg_query($dbconn3, $insert);
  //dump the result object
  var_dump($result);
  // Closing connection
  pg_close($dbconn3);
}
else
{
echo "Hola mundo";
}
?>
