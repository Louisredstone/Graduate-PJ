<?php
    if (isset($_POST['action']))
    {
        $tsk=$_POST['action'];
        switch($tsk){
            case "CPU":
                $log=fopen("LeNet_CPU.log","r") or die("Unable to open file!");
                if (filesize("LeNet_CPU.log")>0){
                    $arr=array();
                    while(!feof($log)){
                        array_push($arr,fgets($log));
                    }
                    $init=0;
                    $ceil=8;
                    $content="";
                    if (count($arr)>$ceil){
                        $init=count($arr)-$ceil;
                    }
                    for($i=$init;$i<count($arr);$i++){
                        $encode = mb_detect_encoding($arr[$i], array("ASCII",'UTF-8',"GB2312","GBK",'BIG5')); 
                        $encoded_line= mb_convert_encoding($arr[$i], 'UTF-8', $encode);
                        $content="{$content}{$encoded_line}<br>";
                    }
                    echo $content;
                }
                fclose($log);
            break;
            case "GPU":
                $log=fopen("LeNet_GPU.log","r") or die("Unable to open file!");
                if (filesize("LeNet_GPU.log")>0){
                    $arr=array();
                    while(!feof($log)){
                        array_push($arr,fgets($log));
                    }
                    $init=0;
                    $ceil=8;
                    $content="";
                    if (count($arr)>$ceil){
                        $init=count($arr)-$ceil;
                    }
                    for($i=$init;$i<count($arr);$i++){
                        $encode = mb_detect_encoding($arr[$i], array("ASCII",'UTF-8',"GB2312","GBK",'BIG5')); 
                        $encoded_line= mb_convert_encoding($arr[$i], 'UTF-8', $encode);
                        $content="{$content}{$encoded_line}<br>";
                    }
                    echo $content;
                }
                fclose($log);
            break;
            case "FPGA":
                $log=fopen("LeNet_FPGA.log","r") or die("Unable to open file!");
                if (filesize("LeNet_FPGA.log")>0){
                    $arr=array();
                    while(!feof($log)){
                        array_push($arr,fgets($log));
                    }
                    $init=0;
                    $ceil=8;
                    $content="";
                    if (count($arr)>$ceil){
                        $init=count($arr)-$ceil;
                    }
                    for($i=$init;$i<count($arr);$i++){
                        $encode = mb_detect_encoding($arr[$i], array("ASCII",'UTF-8',"GB2312","GBK",'BIG5')); 
                        $encoded_line= mb_convert_encoding($arr[$i], 'UTF-8', $encode);
                        $content="{$content}{$encoded_line}<br>";
                    }
                    echo $content;
                }
                fclose($log);
            break;
        }
    }
?>