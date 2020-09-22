<!--
Author     : Reidho Satria
Title      : ReVIP
Desciption : Reverse IP Lookup Tool Based On ViewDNS API
Thanks     : - Pure CSS
             - SevernC0de
-->
<html>
<head>
<title>ReVIP</title>
<!-- META DATA -->
<meta name="author" content="reidhosatria">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="Reverse IP Lookup">
<!-- LINK DATA -->
<link rel="shortcut icon" href="https://raw.githubusercontent.com/reidhosatria/ReVIP/master/icon.png">
<link href="//maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet"></link>
<link rel="stylesheet" href="https://unpkg.com/purecss@1.0.1/build/pure-min.css" integrity="sha384-oAOxQR6DkCoMliIh8yFnu25d7Eq/PHS21PClpwjOTeU2jRSq11vu66rf90/cZr47" crossorigin="anonymous">
<style>
body {
  font-family:Arial;
  background: #ffffff;
  background-image: url(https://raw.githubusercontent.com/reidhosatria/ReVIP/master/bg.jpg);
  background-size: 100% 100%;
  background-position: center;
  background-attachment: fixed;
  background-repeat: no-repeat;
}
a {
  color : darkblue;
}
div.static {
  position: fixed;
  bottom: 0;
  right: 0;
  width: 300px;
}
table {
  background: #ffffff;
}
div img[alt="www.000webhost.com"], div img[alt='www.000webhost.com']
{ display:none;visibility:hidden;
}
</style>
</head>
<body align="center">
<img width="300" src="https://raw.githubusercontent.com/reidhosatria/ReVIP/master/icon.png">
<form method='POST' action=''>
    <input class="pure-button" type='text' name='websitetarget' value='213.186.33.19'>
    <input class="pure-button" type='submit' value='INPUT'><br><br>
</form>
<?php
function curl($url)
{
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "GET");
    $headers   = array();
    $headers[] = 'Authority: api.viewdns.info';
    $headers[] = 'Pragma: no-cache';
    $headers[] = 'Cache-Control: no-cache';
    $headers[] = 'Upgrade-Insecure-Requests: 1';
    $headers[] = 'User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36';
    $headers[] = 'Sec-Fetch-Mode: navigate';
    $headers[] = 'Sec-Fetch-User: ?1';
    $headers[] = 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3';
    $headers[] = 'Sec-Fetch-Site: none';
    $headers[] = 'Accept-Language: en-US,en;q=0.9,id;q=0.8';
    curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    $exec = curl_exec($ch);
    return $exec;
    curl_close($ch);
}
error_reporting(0);
if (isset($_POST['websitetarget'])) {
	$ipkey  = "37308be569fe07583e2bcb13b986d703a906250a"; // change to your dnsview api key
    $websitetargetlu   = $_POST['websitetarget'];
    $sumber = "https://api.viewdns.info/reverseip/?host=" . $websitetargetlu . "&apikey=" . $ipkey . "&output=json&page=15";
    $malink = curl($sumber);
    $json   = json_decode($malink, true);
	$count = count($json['response']['domains']);
	
?>
<table class="pure-table pure-table-horizontal" align="center">
  <tr>
   <th>&nbsp;    Domain Name       &nbsp;</th>
  </tr>
  <?php for ($i=0; $i < $count ; $i++) {  ?>
  <tr>
  <td>&nbsp;<?php echo $json["response"]["domains"][$i]["name"]; ?>&nbsp;</td>
  </tr>
  <?php } ?>
  </table>
  <br>
<?php
}
?>
</body>
<div class="static">
<font align="bottom">Make With <font color="red"><i class="fa fa-heart" aria-hidden="true"></i></font> by <a style="text-decoration:none" href="https://github.com/reidhosatria" target="_BLANK">Reidho</a></font>
</div>
</html>
