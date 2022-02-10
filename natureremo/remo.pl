#! /usr/bin/perl
#
# 家製協AEHAリモコンコードから上記Nature Remo用信号定義データを生成するPerlプログラム
#
# ※curl実行用の出力は"\"のエスケープなどMS-DOSコマンドプロンプト用
#
# C:\>perl aeha-code2nature-remo.pl  aa 5a 8f 12 16 d1
#
# データはコマンド行引数に16進数の列で与える
@data = map { hex($_) & 0xff } @ARGV;

# データを0/1列に変換
$bytes = scalar (@data); $bits = $bytes * 8;
$data = unpack ("b$bits", pack ("C" x $bytes, @data));

# 出力の作成
$f = 38;                # キャリア周波数は38kHz
$t = 0.425 * 1000;      # T=0.425msec

# JSON open
$json  = qq({\n);
$json .= qq("format":"us",\n);
$json .= qq("freq":$f,\n);
$json .= qq("data":[\n);

for ($count = 0; $count < 2; $count++){

    $len = 133 * 1000;      # １送信単位を133msecとする

    # リーダー部 ON(8T)->OFF(4T)
    $json .= (8 * $t) . "," . (4 * $t) . ",\n";
    $len -= 12 * $t;

    # データ部 0:ON(1T)->OFF(1T), 1:ON(1T)->OFF(3T)
    foreach $bit (split ("", $data)) {
        if ($bit eq "0") {
            $json .= (1 * $t) . "," . (1 * $t) . ",";
            $len -= 2 * $t;
        } else {
            $json .= (1 * $t) . "," . (3 * $t) . ",";
            $len -= 4 * $t;
        }
    }

    $json .= "\n";

    # トレーラー部 ON(1T)->OFF(Nmsec) Nはここまでの全体が１送信単位(133msec)になるように決める
    $json .= (1 * $t) . ",";
    $len -= 1 * $t;
    $len = 8 * 1000 if ($len < 8 * 1000); # 最小8msec
    while ($len > 0) {
        if ($len >= 65536) {
            $json .= "65535,0,";
            $len -= 65535;
        } else {
            $json .= "$len";
            last;
        }
    }

    if ($count == 0) {
        $json .= ",";
    }
    $json .= "\n";
}

# JSON close
$json .= "]}\n";

# ベタ書きにしたいとき
$json =~ s/\n//sg;
$json .= "\n";

# 直接コマンド発行
#$json =~ s/\n//sg;
#$json = "curl -X POST \"http://192.168.1.2/messages\" -H \"X-Requested-With: curl\" -H \"accept: application/json\" -d " . "\"$json\"";

# 画面に出力
print "$json\n";

#実行
#system $json;
;