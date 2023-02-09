<html>
<head>
<title>custom_dog.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #cc7832;}
.s1 { color: #a9b7c6;}
.s2 { color: #6a8759;}
.s3 { color: #808080;}
.s4 { color: #6897bb;}
</style>
</head>
<body bgcolor="#2b2b2b">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
custom_dog.py</font>
</center></td></tr></table>
<pre><span class="s0">import </span><span class="s1">random</span>
<span class="s0">from </span><span class="s1">dogclass </span><span class="s0">import </span><span class="s1">Dog</span>

<span class="s0">def </span><span class="s1">Custom_Dog():</span>

    <span class="s1">dna = </span><span class="s2">&quot;&quot;</span>
    <span class="s3"># THIS IS FOR THE COAT COLOR DNA SPECIFICATION</span>
    <span class="s1">print(</span><span class="s2">&quot;CHOOSE BETWEEN THE OPTIONS OF COAT COLORS AVAILABLE&quot;</span><span class="s1">)</span>
    <span class="s1">print(</span><span class="s2">&quot;1 - Black&quot;</span><span class="s1">)</span>
    <span class="s1">print(</span><span class="s2">&quot;2 - Brown&quot;</span><span class="s1">)</span>
    <span class="s1">print(</span><span class="s2">&quot;3 - White&quot;</span><span class="s1">)</span>
    <span class="s1">print(</span><span class="s2">&quot;4 - Merle&quot;</span><span class="s1">)</span>
    <span class="s1">print(</span><span class="s2">&quot;5 - Rare Merle&quot;</span><span class="s1">)</span>
    <span class="s1">print(</span><span class="s2">&quot;6 - Red&quot;</span><span class="s1">)</span>
    <span class="s1">print(</span><span class="s2">&quot;7 - Blue&quot;</span><span class="s1">)</span>
    <span class="s1">color_coat = str(input(</span><span class="s2">&quot;Write the number of the option you desire&quot;</span><span class="s1">))</span>
    <span class="s0">while True</span><span class="s1">:</span>
        <span class="s3"># Black</span>
        <span class="s0">if </span><span class="s1">color_coat == </span><span class="s2">&quot;1&quot;</span><span class="s1">:</span>
            <span class="s1">color_coat_dna = </span><span class="s2">&quot;&quot;</span><span class="s1">.join(random.choices([</span><span class="s2">&quot;BBb&quot;</span><span class="s0">, </span><span class="s2">&quot;BbB&quot;</span><span class="s0">,</span><span class="s2">&quot;bBB&quot;</span><span class="s0">,</span><span class="s2">&quot;BBB&quot;</span><span class="s0">,</span><span class="s2">&quot;BBY&quot;</span><span class="s0">,</span><span class="s2">&quot;BYB&quot;</span><span class="s0">,</span><span class="s2">&quot;YBB&quot;</span><span class="s1">]</span><span class="s0">, </span><span class="s1">k=</span><span class="s4">1</span><span class="s1">))</span>
            <span class="s0">break</span>
        <span class="s3"># Brown</span>
        <span class="s0">if </span><span class="s1">color_coat == </span><span class="s2">&quot;2&quot;</span><span class="s1">:</span>
            <span class="s1">color_coat_dna = </span><span class="s2">&quot;&quot;</span><span class="s1">.join(random.choices([</span><span class="s2">&quot;Bbb&quot;</span><span class="s0">, </span><span class="s2">&quot;bBb&quot;</span><span class="s0">, </span><span class="s2">&quot;bbB&quot;</span><span class="s1">]</span><span class="s0">, </span><span class="s1">k=</span><span class="s4">1</span><span class="s1">))</span>
            <span class="s0">break</span>
        <span class="s3"># White</span>
        <span class="s0">if </span><span class="s1">color_coat == </span><span class="s2">&quot;3&quot;</span><span class="s1">:</span>
            <span class="s1">color_coat_dna = </span><span class="s2">&quot;&quot;</span><span class="s1">.join(random.choices([</span><span class="s2">&quot;bYb&quot;</span><span class="s0">, </span><span class="s2">&quot;Ybb&quot;</span><span class="s0">, </span><span class="s2">&quot;bbY&quot;</span><span class="s0">, </span><span class="s2">&quot;bbb&quot;</span><span class="s1">]</span><span class="s0">, </span><span class="s1">k=</span><span class="s4">1</span><span class="s1">))</span>
            <span class="s0">break</span>
        <span class="s3"># Merle</span>
        <span class="s0">if </span><span class="s1">color_coat == </span><span class="s2">&quot;4&quot;</span><span class="s1">:</span>
            <span class="s1">color_coat_dna = </span><span class="s2">&quot;&quot;</span><span class="s1">.join(random.choices([</span><span class="s2">&quot;YBb&quot;</span><span class="s0">, </span><span class="s2">&quot;BbY&quot;</span><span class="s0">, </span><span class="s2">&quot;bYB&quot;</span><span class="s0">, </span><span class="s2">&quot;YbB&quot;</span><span class="s0">, </span><span class="s2">&quot;bBY&quot;</span><span class="s0">, </span><span class="s2">&quot;BYb&quot;</span><span class="s1">]</span><span class="s0">, </span><span class="s1">k=</span><span class="s4">1</span><span class="s1">))</span>
            <span class="s0">break</span>
        <span class="s3"># Rare Merle</span>
        <span class="s0">if </span><span class="s1">color_coat == </span><span class="s2">&quot;5&quot;</span><span class="s1">:</span>
            <span class="s1">color_coat_dna = </span><span class="s2">&quot;&quot;</span><span class="s1">.join(random.choices([</span><span class="s2">&quot;YYB&quot;</span><span class="s0">, </span><span class="s2">&quot;YBY&quot;</span><span class="s0">, </span><span class="s2">&quot;BYY&quot;</span><span class="s1">]</span><span class="s0">, </span><span class="s1">k=</span><span class="s4">1</span><span class="s1">))</span>
            <span class="s0">break</span>
        <span class="s3"># Red</span>
        <span class="s0">if </span><span class="s1">color_coat == </span><span class="s2">&quot;6&quot;</span><span class="s1">:</span>
            <span class="s1">color_coat_dna = </span><span class="s2">&quot;&quot;</span><span class="s1">.join(random.choices([</span><span class="s2">&quot;YYb&quot;</span><span class="s0">, </span><span class="s2">&quot;bYY&quot;</span><span class="s0">, </span><span class="s2">&quot;YbY&quot;</span><span class="s1">]</span><span class="s0">, </span><span class="s1">k=</span><span class="s4">1</span><span class="s1">))</span>
            <span class="s0">break</span>
        <span class="s3"># Blue</span>
        <span class="s0">if </span><span class="s1">color_coat == </span><span class="s2">&quot;7&quot;</span><span class="s1">:</span>
            <span class="s1">color_coat_dna = </span><span class="s2">&quot;&quot;</span><span class="s1">.join(random.choices([</span><span class="s2">&quot;YYY&quot;</span><span class="s1">]</span><span class="s0">, </span><span class="s1">k=</span><span class="s4">1</span><span class="s1">))</span>
            <span class="s0">break</span>
        <span class="s0">else</span><span class="s1">:</span>
            <span class="s1">print(</span><span class="s2">&quot;Wrong value, please assign a new one&quot;</span><span class="s1">)</span>
            <span class="s1">color_coat = str(input(</span><span class="s2">&quot;Write the number of the option you desire&quot;</span><span class="s1">))</span>

    <span class="s3"># THIS IS FOR THE EYE COLOR DNA SPECIFICATION</span>

    <span class="s1">print(</span><span class="s2">&quot;CHOOSE BETWEEN THE OPTIONS AVAILABLE&quot;</span><span class="s1">)</span>
    <span class="s1">print(</span><span class="s2">&quot;1 - Blue&quot;</span><span class="s1">)</span>
    <span class="s1">print(</span><span class="s2">&quot;2 - Brown&quot;</span><span class="s1">)</span>
    <span class="s1">print(</span><span class="s2">&quot;3 - Green&quot;</span><span class="s1">)</span>
    <span class="s1">print(</span><span class="s2">&quot;4 - light brown&quot;</span><span class="s1">)</span>
    <span class="s1">print(</span><span class="s2">&quot;5 - Dark Green&quot;</span><span class="s1">)</span>
    <span class="s1">print(</span><span class="s2">&quot;6 - Yellow&quot;</span><span class="s1">)</span>
    <span class="s1">print(</span><span class="s2">&quot;7 - Golden&quot;</span><span class="s1">)</span>
    <span class="s1">eye_color = str(input(</span><span class="s2">&quot;Write the number of the option you desire&quot;</span><span class="s1">))</span>
    <span class="s0">while True</span><span class="s1">:</span>
        <span class="s3"># Blue</span>
        <span class="s0">if </span><span class="s1">eye_color == </span><span class="s2">&quot;1&quot;</span><span class="s1">:</span>
            <span class="s1">eye_color_dna = </span><span class="s2">&quot;&quot;</span><span class="s1">.join(random.choices([</span><span class="s2">&quot;BBb&quot;</span><span class="s0">, </span><span class="s2">&quot;BbB&quot;</span><span class="s0">, </span><span class="s2">&quot;bBB&quot;</span><span class="s0">, </span><span class="s2">&quot;BBB&quot;</span><span class="s0">, </span><span class="s2">&quot;BBY&quot;</span><span class="s0">, </span><span class="s2">&quot;BYB&quot;</span><span class="s0">, </span><span class="s2">&quot;YBB&quot;</span><span class="s1">]</span><span class="s0">, </span><span class="s1">k=</span><span class="s4">1</span><span class="s1">))</span>
            <span class="s0">break</span>
        <span class="s3"># Brown</span>
        <span class="s0">if </span><span class="s1">eye_color == </span><span class="s2">&quot;2&quot;</span><span class="s1">:</span>
            <span class="s1">eye_color_dna = </span><span class="s2">&quot;&quot;</span><span class="s1">.join(random.choices([</span><span class="s2">&quot;Bbb&quot;</span><span class="s0">, </span><span class="s2">&quot;bBb&quot;</span><span class="s0">, </span><span class="s2">&quot;bbB&quot;</span><span class="s1">]</span><span class="s0">, </span><span class="s1">k=</span><span class="s4">1</span><span class="s1">))</span>
            <span class="s0">break</span>
        <span class="s3"># White</span>
        <span class="s0">if </span><span class="s1">eye_color == </span><span class="s2">&quot;3&quot;</span><span class="s1">:</span>
            <span class="s1">eye_color_dna = </span><span class="s2">&quot;&quot;</span><span class="s1">.join(random.choices([</span><span class="s2">&quot;bYb&quot;</span><span class="s0">, </span><span class="s2">&quot;Ybb&quot;</span><span class="s0">, </span><span class="s2">&quot;bbY&quot;</span><span class="s0">, </span><span class="s2">&quot;bbb&quot;</span><span class="s1">]</span><span class="s0">, </span><span class="s1">k=</span><span class="s4">1</span><span class="s1">))</span>
            <span class="s0">break</span>
        <span class="s3"># Merle</span>
        <span class="s0">if </span><span class="s1">eye_color == </span><span class="s2">&quot;4&quot;</span><span class="s1">:</span>
            <span class="s1">eye_color_dna = </span><span class="s2">&quot;&quot;</span><span class="s1">.join(random.choices([</span><span class="s2">&quot;YBb&quot;</span><span class="s0">, </span><span class="s2">&quot;BbY&quot;</span><span class="s0">, </span><span class="s2">&quot;bYB&quot;</span><span class="s0">, </span><span class="s2">&quot;YbB&quot;</span><span class="s0">, </span><span class="s2">&quot;bBY&quot;</span><span class="s0">, </span><span class="s2">&quot;BYb&quot;</span><span class="s1">]</span><span class="s0">, </span><span class="s1">k=</span><span class="s4">1</span><span class="s1">))</span>
            <span class="s0">break</span>
        <span class="s3"># Rare Merle</span>
        <span class="s0">if </span><span class="s1">eye_color == </span><span class="s2">&quot;5&quot;</span><span class="s1">:</span>
            <span class="s1">eye_color_dna = </span><span class="s2">&quot;&quot;</span><span class="s1">.join(random.choices([</span><span class="s2">&quot;YYB&quot;</span><span class="s0">, </span><span class="s2">&quot;YBY&quot;</span><span class="s0">, </span><span class="s2">&quot;BYY&quot;</span><span class="s1">]</span><span class="s0">, </span><span class="s1">k=</span><span class="s4">1</span><span class="s1">))</span>
            <span class="s0">break</span>
        <span class="s3"># Red</span>
        <span class="s0">if </span><span class="s1">eye_color == </span><span class="s2">&quot;6&quot;</span><span class="s1">:</span>
            <span class="s1">eye_color_dna = </span><span class="s2">&quot;&quot;</span><span class="s1">.join(random.choices([</span><span class="s2">&quot;YYb&quot;</span><span class="s0">, </span><span class="s2">&quot;bYY&quot;</span><span class="s0">, </span><span class="s2">&quot;YbY&quot;</span><span class="s1">]</span><span class="s0">, </span><span class="s1">k=</span><span class="s4">1</span><span class="s1">))</span>
            <span class="s0">break</span>
        <span class="s3"># Blue</span>
        <span class="s0">if </span><span class="s1">eye_color == </span><span class="s2">&quot;7&quot;</span><span class="s1">:</span>
            <span class="s1">eye_color_dna = </span><span class="s2">&quot;&quot;</span><span class="s1">.join(random.choices([</span><span class="s2">&quot;YYY&quot;</span><span class="s1">]</span><span class="s0">, </span><span class="s1">k=</span><span class="s4">1</span><span class="s1">))</span>
            <span class="s0">break</span>
        <span class="s0">else</span><span class="s1">:</span>
            <span class="s1">print(</span><span class="s2">&quot;Wrong value, please assign a new one&quot;</span><span class="s1">)</span>
            <span class="s1">eye_color = str(input(</span><span class="s2">&quot;Write the number of the option you desire&quot;</span><span class="s1">))</span>
    <span class="s3"># THIS IS FOR coat type DNA SPECIFICATION</span>

    <span class="s1">print(</span><span class="s2">&quot;CHOOSE BETWEEN THE OPTIONS AVAILABLE&quot;</span><span class="s1">)</span>
    <span class="s1">print(</span><span class="s2">&quot;1 - Short&quot;</span><span class="s1">)</span>
    <span class="s1">print(</span><span class="s2">&quot;2 - Long&quot;</span><span class="s1">)</span>
    <span class="s1">print(</span><span class="s2">&quot;3 - Medium&quot;</span><span class="s1">)</span>
    <span class="s1">print(</span><span class="s2">&quot;4 - Curly&quot;</span><span class="s1">)</span>
    <span class="s1">print(</span><span class="s2">&quot;5 - Very Long&quot;</span><span class="s1">)</span>
    <span class="s1">print(</span><span class="s2">&quot;6 - Bushy&quot;</span><span class="s1">)</span>
    <span class="s1">print(</span><span class="s2">&quot;7 - Silky&quot;</span><span class="s1">)</span>
    <span class="s1">type_coat = str(input(</span><span class="s2">&quot;Write the number of the option you desire&quot;</span><span class="s1">))</span>
    <span class="s0">while True</span><span class="s1">:</span>
        <span class="s3"># Black</span>
        <span class="s0">if </span><span class="s1">type_coat == </span><span class="s2">&quot;1&quot;</span><span class="s1">:</span>
            <span class="s1">type_coat_dna = </span><span class="s2">&quot;&quot;</span><span class="s1">.join(random.choices([</span><span class="s2">&quot;BBb&quot;</span><span class="s0">, </span><span class="s2">&quot;BbB&quot;</span><span class="s0">, </span><span class="s2">&quot;bBB&quot;</span><span class="s0">, </span><span class="s2">&quot;BBB&quot;</span><span class="s0">, </span><span class="s2">&quot;BBY&quot;</span><span class="s0">, </span><span class="s2">&quot;BYB&quot;</span><span class="s0">, </span><span class="s2">&quot;YBB&quot;</span><span class="s1">]</span><span class="s0">, </span><span class="s1">k=</span><span class="s4">1</span><span class="s1">))</span>
            <span class="s0">break</span>
        <span class="s3"># Brown</span>
        <span class="s0">if </span><span class="s1">type_coat == </span><span class="s2">&quot;2&quot;</span><span class="s1">:</span>
            <span class="s1">type_coat_dna = </span><span class="s2">&quot;&quot;</span><span class="s1">.join(random.choices([</span><span class="s2">&quot;Bbb&quot;</span><span class="s0">, </span><span class="s2">&quot;bBb&quot;</span><span class="s0">, </span><span class="s2">&quot;bbB&quot;</span><span class="s1">]</span><span class="s0">, </span><span class="s1">k=</span><span class="s4">1</span><span class="s1">))</span>
            <span class="s0">break</span>
        <span class="s3"># White</span>
        <span class="s0">if </span><span class="s1">type_coat == </span><span class="s2">&quot;3&quot;</span><span class="s1">:</span>
            <span class="s1">type_coat_dna = </span><span class="s2">&quot;&quot;</span><span class="s1">.join(random.choices([</span><span class="s2">&quot;bYb&quot;</span><span class="s0">, </span><span class="s2">&quot;Ybb&quot;</span><span class="s0">, </span><span class="s2">&quot;bbY&quot;</span><span class="s0">, </span><span class="s2">&quot;bbb&quot;</span><span class="s1">]</span><span class="s0">, </span><span class="s1">k=</span><span class="s4">1</span><span class="s1">))</span>
            <span class="s0">break</span>
        <span class="s3"># Merle</span>
        <span class="s0">if </span><span class="s1">type_coat == </span><span class="s2">&quot;4&quot;</span><span class="s1">:</span>
            <span class="s1">type_coat_dna = </span><span class="s2">&quot;&quot;</span><span class="s1">.join(random.choices([</span><span class="s2">&quot;YBb&quot;</span><span class="s0">, </span><span class="s2">&quot;BbY&quot;</span><span class="s0">, </span><span class="s2">&quot;bYB&quot;</span><span class="s0">, </span><span class="s2">&quot;YbB&quot;</span><span class="s0">, </span><span class="s2">&quot;bBY&quot;</span><span class="s0">, </span><span class="s2">&quot;BYb&quot;</span><span class="s1">]</span><span class="s0">, </span><span class="s1">k=</span><span class="s4">1</span><span class="s1">))</span>
            <span class="s0">break</span>
        <span class="s3"># Rare Merle</span>
        <span class="s0">if </span><span class="s1">type_coat == </span><span class="s2">&quot;5&quot;</span><span class="s1">:</span>
            <span class="s1">type_coat_dna = </span><span class="s2">&quot;&quot;</span><span class="s1">.join(random.choices([</span><span class="s2">&quot;YYB&quot;</span><span class="s0">, </span><span class="s2">&quot;YBY&quot;</span><span class="s0">, </span><span class="s2">&quot;BYY&quot;</span><span class="s1">]</span><span class="s0">, </span><span class="s1">k=</span><span class="s4">1</span><span class="s1">))</span>
            <span class="s0">break</span>
        <span class="s3"># Red</span>
        <span class="s0">if </span><span class="s1">type_coat == </span><span class="s2">&quot;6&quot;</span><span class="s1">:</span>
            <span class="s1">type_coat_dna = </span><span class="s2">&quot;&quot;</span><span class="s1">.join(random.choices([</span><span class="s2">&quot;YYb&quot;</span><span class="s0">, </span><span class="s2">&quot;bYY&quot;</span><span class="s0">, </span><span class="s2">&quot;YbY&quot;</span><span class="s1">]</span><span class="s0">, </span><span class="s1">k=</span><span class="s4">1</span><span class="s1">))</span>
            <span class="s0">break</span>
        <span class="s3"># Blue</span>
        <span class="s0">if </span><span class="s1">type_coat == </span><span class="s2">&quot;7&quot;</span><span class="s1">:</span>
            <span class="s1">type_coat_dna = </span><span class="s2">&quot;&quot;</span><span class="s1">.join(random.choices([</span><span class="s2">&quot;YYY&quot;</span><span class="s1">]</span><span class="s0">, </span><span class="s1">k=</span><span class="s4">1</span><span class="s1">))</span>
            <span class="s0">break</span>
        <span class="s0">else</span><span class="s1">:</span>
            <span class="s1">print(</span><span class="s2">&quot;Wrong value, please assign a new one&quot;</span><span class="s1">)</span>
            <span class="s1">type_coat = str(input(</span><span class="s2">&quot;Write the number of the option you desire&quot;</span><span class="s1">))</span>


    <span class="s3"># THIS IS FOR coat type DNA SPECIFICATION</span>

    <span class="s1">print(</span><span class="s2">&quot;CHOOSE BETWEEN THE OPTIONS AVAILABLE&quot;</span><span class="s1">)</span>
    <span class="s1">print(</span><span class="s2">&quot;1 - Male&quot;</span><span class="s1">)</span>
    <span class="s1">print(</span><span class="s2">&quot;2 - Female&quot;</span><span class="s1">)</span>

    <span class="s1">sex = str(input(</span><span class="s2">&quot;Write the number of the option you desire&quot;</span><span class="s1">))</span>
    <span class="s0">while True</span><span class="s1">:</span>
        <span class="s3"># Black</span>
        <span class="s0">if </span><span class="s1">sex == </span><span class="s2">&quot;1&quot;</span><span class="s1">:</span>
            <span class="s1">sex_dna = </span><span class="s2">&quot;&quot;</span><span class="s1">.join(random.choices([</span><span class="s2">&quot;XZ&quot;</span><span class="s0">,</span><span class="s2">&quot;ZX&quot;</span><span class="s1">]</span><span class="s0">, </span><span class="s1">k=</span><span class="s4">1</span><span class="s1">))</span>
            <span class="s0">break</span>
        <span class="s3"># Brown</span>
        <span class="s0">if </span><span class="s1">sex == </span><span class="s2">&quot;2&quot;</span><span class="s1">:</span>
            <span class="s1">sex_dna = </span><span class="s2">&quot;&quot;</span><span class="s1">.join(random.choices([</span><span class="s2">&quot;XX&quot;</span><span class="s1">]</span><span class="s0">, </span><span class="s1">k=</span><span class="s4">1</span><span class="s1">))</span>
            <span class="s0">break</span>
        <span class="s0">else</span><span class="s1">:</span>
            <span class="s1">print(</span><span class="s2">&quot;Wrong value, please assign a new one&quot;</span><span class="s1">)</span>
            <span class="s1">sex = str(input(</span><span class="s2">&quot;Write the number of the option you desire&quot;</span><span class="s1">))</span>

    <span class="s1">dna = color_coat_dna + eye_color_dna + type_coat_dna + sex_dna</span>

    <span class="s1">dog_name = str(input(</span><span class="s2">&quot;Insert new custom dog name here: &quot;</span><span class="s1">))</span>
    <span class="s1">NewDog = Dog(dog_name</span><span class="s0">, </span><span class="s1">dna)</span>
    <span class="s0">return </span><span class="s1">NewDog</span></pre>
</body>
</html>