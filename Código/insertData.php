<?php /*
 * PHP PGSQL - How to insert rows into PostgreSQL table
 */
$humedad = $_POST["humedad"];
$caudal = $_POST["caudal"];
$fecha = $_POST["fecha"];

if(isset($_POST["humedad"]))
{
  $dbconn3 = pg_connect("host=bri2.utalca.cl port=5432 dbname=Soilmap user=nmaturana password=nmaturana");
  $humedad = $_POST["humedad"];
  $caudal = $_POST["caudal"];
  $fecha = $_POST["fecha"];
  $insert = "INSERT INTO registros(humedad, caudal, fecha) VALUES('".$humedad."', '".$caudal."', '".$fecha."')";
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