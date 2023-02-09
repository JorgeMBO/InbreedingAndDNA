<html>
<head>
<title>dogclass.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #cc7832;}
.s1 { color: #a9b7c6;}
.s2 { color: #6a8759;}
.s3 { color: #808080;}
.s4 { color: #6897bb;}
.s5 { color: #629755; font-style: italic;}
</style>
</head>
<body bgcolor="#2b2b2b">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
dogclass.py</font>
</center></td></tr></table>
<pre><span class="s0">import </span><span class="s1">random</span>



<span class="s0">class </span><span class="s1">Dog:</span>

    <span class="s0">def </span><span class="s1">__init__(self</span><span class="s0">, </span><span class="s1">name=</span><span class="s2">&quot;&quot;</span><span class="s0">, </span><span class="s1">dna=</span><span class="s0">None,</span><span class="s1">mother=</span><span class="s0">None, </span><span class="s1">father=</span><span class="s0">None, </span><span class="s1">color_coat=</span><span class="s0">None, </span><span class="s1">color_eyes=</span><span class="s0">None, </span><span class="s1">coat_type=</span><span class="s0">None</span><span class="s1">):</span>
        <span class="s1">self.name = name</span>
        <span class="s1">self.color_coat = color_coat</span>
        <span class="s1">self.color_eyes = color_eyes</span>
        <span class="s1">self.coat_type = coat_type</span>
        <span class="s1">self.mother = mother</span>
        <span class="s1">self.father = father</span>
        <span class="s1">self.siblings = []</span>
        <span class="s1">self.offspring = []</span>
        <span class="s1">self.dna = dna</span>
        <span class="s1">self.mutated = </span><span class="s0">False</span>


        <span class="s0">if </span><span class="s1">self.dna </span><span class="s0">is None</span><span class="s1">:</span>
            <span class="s1">self.color_coat = </span><span class="s2">&quot;unknown&quot;</span>
            <span class="s1">self.color_eyes = </span><span class="s2">&quot;unknown&quot;</span>
            <span class="s1">self.coat_type = </span><span class="s2">&quot;unknown&quot;</span>
            <span class="s1">self.sex = </span><span class="s2">&quot;unknown&quot;</span>
            <span class="s3"># If no DNA is specified, randomly generate it</span>
            <span class="s1">self.dna = self.generate_dna()</span>
        <span class="s0">else</span><span class="s1">:</span>
            <span class="s1">self.color_coat = self.dna_to_color_coat(self.dna[:</span><span class="s4">3</span><span class="s1">])</span>
            <span class="s1">self.color_eyes = self.dna_to_color_eyes(self.dna[</span><span class="s4">3</span><span class="s1">:</span><span class="s4">6</span><span class="s1">])</span>
            <span class="s1">self.coat_type = self.dna_to_coat_type(self.dna[</span><span class="s4">6</span><span class="s1">:</span><span class="s4">9</span><span class="s1">])</span>
            <span class="s1">self.sex = self.dna_to_sex(self.dna[</span><span class="s4">9</span><span class="s1">:</span><span class="s4">11</span><span class="s1">])</span>

        <span class="s1">self.color_coat = self.dna_to_color_coat(self.dna[:</span><span class="s4">3</span><span class="s1">])</span>
        <span class="s1">self.color_eyes = self.dna_to_color_eyes(self.dna[</span><span class="s4">3</span><span class="s1">:</span><span class="s4">6</span><span class="s1">])</span>
        <span class="s1">self.coat_type = self.dna_to_coat_type(self.dna[</span><span class="s4">6</span><span class="s1">:</span><span class="s4">9</span><span class="s1">])</span>
        <span class="s1">self.sex = self.dna_to_sex(self.dna[</span><span class="s4">9</span><span class="s1">:</span><span class="s4">11</span><span class="s1">])</span>

    <span class="s0">def </span><span class="s1">__str__(self):</span>
        <span class="s0">if </span><span class="s1">self.name == </span><span class="s0">None</span><span class="s1">:</span>
            <span class="s1">self.name = </span><span class="s2">&quot;GIVE THIS DOG A NAME&quot;</span>
        <span class="s0">return </span><span class="s1">self.name + </span><span class="s2">&quot; score: &quot; </span><span class="s1">+ str(self.score)</span>

    <span class="s0">def </span><span class="s1">attribute_score(self):</span>
        <span class="s5">&quot;&quot;&quot;Calculate the attribute score of the dog&quot;&quot;&quot;</span>
        <span class="s1">score = </span><span class="s4">0</span>
        <span class="s0">if </span><span class="s1">self.color_coat == </span><span class="s2">&quot;black&quot;</span><span class="s1">:</span>
            <span class="s1">score += </span><span class="s4">10</span>
        <span class="s0">if </span><span class="s1">self.color_eyes == </span><span class="s2">&quot;blue&quot;</span><span class="s1">:</span>
            <span class="s1">score += </span><span class="s4">5</span>
        <span class="s0">if </span><span class="s1">self.coat_type == </span><span class="s2">&quot;Long&quot;</span><span class="s1">:</span>
            <span class="s1">score += </span><span class="s4">8</span>
        <span class="s1">self.score = score</span>
        <span class="s0">return </span><span class="s1">score</span>

    <span class="s0">def </span><span class="s1">generate_dna(self):</span>

        <span class="s0">if </span><span class="s1">self.mother </span><span class="s0">is not None and </span><span class="s1">self.father </span><span class="s0">is not None</span><span class="s1">:</span>
            <span class="s3"># Determine the DNA sequence for the coat color based on the parents' DNA</span>
            <span class="s1">mother_coat_dna = self.mother.dna[:</span><span class="s4">3</span><span class="s1">]</span>
            <span class="s1">father_coat_dna = self.father.dna[:</span><span class="s4">3</span><span class="s1">]</span>
            <span class="s1">coat_dna = </span><span class="s2">&quot;&quot;</span>
            <span class="s0">for </span><span class="s1">i </span><span class="s0">in </span><span class="s1">range(</span><span class="s4">3</span><span class="s1">):</span>
                <span class="s0">if </span><span class="s1">random.random() &lt; </span><span class="s4">0.5</span><span class="s1">:</span>
                    <span class="s1">coat_dna += mother_coat_dna[i]</span>
                <span class="s0">else</span><span class="s1">:</span>
                    <span class="s1">coat_dna += father_coat_dna[i]</span>

            <span class="s3"># Determine the DNA sequence for the eye color based on the parents' DNA</span>
            <span class="s1">mother_eyes_dna = self.mother.dna[</span><span class="s4">3</span><span class="s1">:</span><span class="s4">6</span><span class="s1">]</span>
            <span class="s1">father_eyes_dna = self.father.dna[</span><span class="s4">3</span><span class="s1">:</span><span class="s4">6</span><span class="s1">]</span>
            <span class="s1">eyes_dna = </span><span class="s2">&quot;&quot;</span>
            <span class="s0">for </span><span class="s1">i </span><span class="s0">in </span><span class="s1">range(</span><span class="s4">3</span><span class="s1">):</span>
                <span class="s0">if </span><span class="s1">random.random() &lt; </span><span class="s4">0.5</span><span class="s1">:</span>
                    <span class="s1">eyes_dna += mother_eyes_dna[i]</span>
                <span class="s0">else</span><span class="s1">:</span>
                    <span class="s1">eyes_dna += father_eyes_dna[i]</span>

            <span class="s3"># Determine the DNA sequence for the coat type based on the parents' DNA</span>
            <span class="s1">mother_coat_type_dna = self.mother.dna[</span><span class="s4">6</span><span class="s1">:]</span>
            <span class="s1">father_coat_type_dna = self.father.dna[</span><span class="s4">6</span><span class="s1">:]</span>
            <span class="s1">coat_type_dna = </span><span class="s2">&quot;&quot;</span>
            <span class="s0">for </span><span class="s1">i </span><span class="s0">in </span><span class="s1">range(</span><span class="s4">3</span><span class="s1">):</span>
                <span class="s0">if </span><span class="s1">random.random() &lt; </span><span class="s4">0.5</span><span class="s1">:</span>
                    <span class="s1">coat_type_dna += mother_coat_type_dna[i]</span>
                <span class="s0">else</span><span class="s1">:</span>
                    <span class="s1">coat_type_dna += father_coat_type_dna[i]</span>

            <span class="s1">mother_sex_dna = self.mother.dna[</span><span class="s4">9</span><span class="s1">:]</span>
            <span class="s1">father_sex_dna = self.father.dna[</span><span class="s4">9</span><span class="s1">:]</span>
            <span class="s1">sex_dna = </span><span class="s2">&quot;&quot;</span>
            <span class="s0">for </span><span class="s1">i </span><span class="s0">in </span><span class="s1">range(</span><span class="s4">2</span><span class="s1">):</span>
                <span class="s0">if </span><span class="s1">random.random() &lt; </span><span class="s4">0.5</span><span class="s1">:</span>
                    <span class="s1">sex_dna += mother_sex_dna[i]</span>
                <span class="s0">else</span><span class="s1">:</span>
                    <span class="s1">sex_dna += father_sex_dna[i]</span>

            <span class="s0">return </span><span class="s1">coat_dna + eyes_dna + coat_type_dna + sex_dna</span>
        <span class="s0">else</span><span class="s1">:</span>
            <span class="s3"># If no mother or father is specified, randomly generate the DNA</span>
            <span class="s0">if </span><span class="s1">random.random() &lt; </span><span class="s4">0.2</span><span class="s1">:</span>
                <span class="s1">self.dna = </span><span class="s2">&quot;&quot;</span><span class="s1">.join(random.choices([</span><span class="s2">&quot;B&quot;</span><span class="s0">, </span><span class="s2">&quot;b&quot;</span><span class="s0">, </span><span class="s2">&quot;Y&quot;</span><span class="s1">]</span><span class="s0">, </span><span class="s1">k=</span><span class="s4">9</span><span class="s1">))</span>
                <span class="s1">choices = [</span><span class="s2">&quot;Z&quot;</span><span class="s0">, </span><span class="s2">&quot;X&quot;</span><span class="s1">]</span>
            <span class="s0">else</span><span class="s1">:</span>
                <span class="s1">self.dna = </span><span class="s2">&quot;&quot;</span><span class="s1">.join(random.choices([</span><span class="s2">&quot;B&quot;</span><span class="s0">, </span><span class="s2">&quot;b&quot;</span><span class="s1">]</span><span class="s0">, </span><span class="s1">k=</span><span class="s4">9</span><span class="s1">))</span>
                <span class="s1">choices = [</span><span class="s2">&quot;Z&quot;</span><span class="s0">, </span><span class="s2">&quot;X&quot;</span><span class="s1">]</span>
            <span class="s1">self.dna += </span><span class="s2">&quot;&quot;</span><span class="s1">.join(random.choices(choices</span><span class="s0">, </span><span class="s1">k=</span><span class="s4">1</span><span class="s1">))</span>
            <span class="s0">if </span><span class="s2">&quot;Z&quot; </span><span class="s0">in </span><span class="s1">self.dna:</span>
                <span class="s1">choices.remove(</span><span class="s2">&quot;Z&quot;</span><span class="s1">)</span>
                <span class="s1">self.dna += </span><span class="s2">&quot;&quot;</span><span class="s1">.join(random.choices(choices</span><span class="s0">, </span><span class="s1">k=</span><span class="s4">1</span><span class="s1">))</span>
            <span class="s0">else</span><span class="s1">:</span>
                <span class="s1">self.dna += </span><span class="s2">&quot;&quot;</span><span class="s1">.join(random.choices(choices</span><span class="s0">, </span><span class="s1">k=</span><span class="s4">1</span><span class="s1">))</span>


        <span class="s0">return </span><span class="s1">self.dna</span>

    <span class="s0">def </span><span class="s1">dna_to_sex(self</span><span class="s0">,</span><span class="s1">dna):</span>
        <span class="s1">sex_mapping ={</span>
            <span class="s2">&quot;XX&quot;</span><span class="s1">: </span><span class="s2">&quot;Female&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;XZ&quot;</span><span class="s1">: </span><span class="s2">&quot;Male&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;ZX&quot;</span><span class="s1">: </span><span class="s2">&quot;Male&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;ZZ&quot;</span><span class="s1">: </span><span class="s2">&quot;Error&quot;</span><span class="s0">,</span>
        <span class="s1">}</span>
        <span class="s0">return </span><span class="s1">sex_mapping.get(dna</span><span class="s0">, </span><span class="s2">&quot;unknown&quot;</span><span class="s1">)</span>


    <span class="s0">def </span><span class="s1">dna_to_color_coat(self</span><span class="s0">, </span><span class="s1">dna):</span>
        <span class="s1">color_coat_mapping = {</span>
            <span class="s2">&quot;BBB&quot;</span><span class="s1">: </span><span class="s2">&quot;black&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;BbB&quot;</span><span class="s1">: </span><span class="s2">&quot;black&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;bBB&quot;</span><span class="s1">: </span><span class="s2">&quot;black&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;BBb&quot;</span><span class="s1">: </span><span class="s2">&quot;black&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;Bbb&quot;</span><span class="s1">: </span><span class="s2">&quot;brown&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;bBb&quot;</span><span class="s1">: </span><span class="s2">&quot;brown&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;bbB&quot;</span><span class="s1">: </span><span class="s2">&quot;brown&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;bbb&quot;</span><span class="s1">: </span><span class="s2">&quot;white&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;YYY&quot;</span><span class="s1">: </span><span class="s2">&quot;blue&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;bYY&quot;</span><span class="s1">: </span><span class="s2">&quot;red&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;YYb&quot;</span><span class="s1">: </span><span class="s2">&quot;red&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;YbY&quot;</span><span class="s1">: </span><span class="s2">&quot;red&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;YYB&quot;</span><span class="s1">: </span><span class="s2">&quot;Rare Merle&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;BYY&quot;</span><span class="s1">: </span><span class="s2">&quot;Rare Merle&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;YBY&quot;</span><span class="s1">: </span><span class="s2">&quot;Rare Merle&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;bbY&quot;</span><span class="s1">: </span><span class="s2">&quot;white&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;bYb&quot;</span><span class="s1">: </span><span class="s2">&quot;white&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;Ybb&quot;</span><span class="s1">: </span><span class="s2">&quot;white&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;YBB&quot;</span><span class="s1">: </span><span class="s2">&quot;black&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;BYB&quot;</span><span class="s1">: </span><span class="s2">&quot;black&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;BBY&quot;</span><span class="s1">: </span><span class="s2">&quot;black&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;BbY&quot;</span><span class="s1">: </span><span class="s2">&quot;Merle&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;bBY&quot;</span><span class="s1">: </span><span class="s2">&quot;Merle&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;BYb&quot;</span><span class="s1">: </span><span class="s2">&quot;Merle&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;bYB&quot;</span><span class="s1">: </span><span class="s2">&quot;Merle&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;YBb&quot;</span><span class="s1">: </span><span class="s2">&quot;Merle&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;YbB&quot;</span><span class="s1">: </span><span class="s2">&quot;Merle&quot;</span><span class="s0">,</span>

        <span class="s1">}</span>
        <span class="s0">return </span><span class="s1">color_coat_mapping.get(dna</span><span class="s0">, </span><span class="s2">&quot;unknown&quot;</span><span class="s1">)</span>

    <span class="s0">def </span><span class="s1">dna_to_color_eyes(self</span><span class="s0">, </span><span class="s1">dna):</span>
        <span class="s1">color_eyes_mapping = {</span>
            <span class="s2">&quot;BBB&quot;</span><span class="s1">: </span><span class="s2">&quot;blue&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;BbB&quot;</span><span class="s1">: </span><span class="s2">&quot;blue&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;bBB&quot;</span><span class="s1">: </span><span class="s2">&quot;blue&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;BBb&quot;</span><span class="s1">: </span><span class="s2">&quot;blue&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;Bbb&quot;</span><span class="s1">: </span><span class="s2">&quot;brown&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;bBb&quot;</span><span class="s1">: </span><span class="s2">&quot;brown&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;bbB&quot;</span><span class="s1">: </span><span class="s2">&quot;brown&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;bbb&quot;</span><span class="s1">: </span><span class="s2">&quot;green&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;YYY&quot;</span><span class="s1">: </span><span class="s2">&quot;golden&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;bYY&quot;</span><span class="s1">: </span><span class="s2">&quot;yellow&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;YYb&quot;</span><span class="s1">: </span><span class="s2">&quot;yellow&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;YbY&quot;</span><span class="s1">: </span><span class="s2">&quot;yellow&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;YYB&quot;</span><span class="s1">: </span><span class="s2">&quot;Dark Green&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;BYY&quot;</span><span class="s1">: </span><span class="s2">&quot;Dark Green&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;YBY&quot;</span><span class="s1">: </span><span class="s2">&quot;Dark Green&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;bbY&quot;</span><span class="s1">: </span><span class="s2">&quot;green&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;bYb&quot;</span><span class="s1">: </span><span class="s2">&quot;green&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;Ybb&quot;</span><span class="s1">: </span><span class="s2">&quot;green&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;YBB&quot;</span><span class="s1">: </span><span class="s2">&quot;blue&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;BYB&quot;</span><span class="s1">: </span><span class="s2">&quot;blue&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;BBY&quot;</span><span class="s1">: </span><span class="s2">&quot;blue&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;BbY&quot;</span><span class="s1">: </span><span class="s2">&quot;light brown&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;bBY&quot;</span><span class="s1">: </span><span class="s2">&quot;light brown&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;BYb&quot;</span><span class="s1">: </span><span class="s2">&quot;light brown&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;bYB&quot;</span><span class="s1">: </span><span class="s2">&quot;light brown&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;YBb&quot;</span><span class="s1">: </span><span class="s2">&quot;light brown&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;YbB&quot;</span><span class="s1">: </span><span class="s2">&quot;dark brown&quot;</span><span class="s0">,</span>
        <span class="s1">}</span>
        <span class="s0">return </span><span class="s1">color_eyes_mapping.get(dna</span><span class="s0">, </span><span class="s2">&quot;unknown&quot;</span><span class="s1">)</span>

    <span class="s0">def </span><span class="s1">dna_to_coat_type(self</span><span class="s0">, </span><span class="s1">dna):</span>
        <span class="s1">coat_type_mapping = {</span>
            <span class="s2">&quot;BBB&quot;</span><span class="s1">: </span><span class="s2">&quot;Short&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;BbB&quot;</span><span class="s1">: </span><span class="s2">&quot;Short&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;bBB&quot;</span><span class="s1">: </span><span class="s2">&quot;Short&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;BBb&quot;</span><span class="s1">: </span><span class="s2">&quot;Short&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;Bbb&quot;</span><span class="s1">: </span><span class="s2">&quot;Long&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;bBb&quot;</span><span class="s1">: </span><span class="s2">&quot;Long&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;bbB&quot;</span><span class="s1">: </span><span class="s2">&quot;Long&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;bbb&quot;</span><span class="s1">: </span><span class="s2">&quot;Medium&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;YYY&quot;</span><span class="s1">: </span><span class="s2">&quot;Silky&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;bYY&quot;</span><span class="s1">: </span><span class="s2">&quot;Bushy&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;YYb&quot;</span><span class="s1">: </span><span class="s2">&quot;Bushy&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;YbY&quot;</span><span class="s1">: </span><span class="s2">&quot;Bushy&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;YYB&quot;</span><span class="s1">: </span><span class="s2">&quot;Very Long&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;BYY&quot;</span><span class="s1">: </span><span class="s2">&quot;Very long&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;YBY&quot;</span><span class="s1">: </span><span class="s2">&quot;Very Long&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;bbY&quot;</span><span class="s1">: </span><span class="s2">&quot;Medium&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;bYb&quot;</span><span class="s1">: </span><span class="s2">&quot;Medium&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;Ybb&quot;</span><span class="s1">: </span><span class="s2">&quot;Medium&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;YBB&quot;</span><span class="s1">: </span><span class="s2">&quot;Short&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;BYB&quot;</span><span class="s1">: </span><span class="s2">&quot;Short&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;BBY&quot;</span><span class="s1">: </span><span class="s2">&quot;Short&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;BbY&quot;</span><span class="s1">: </span><span class="s2">&quot;Curly&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;bBY&quot;</span><span class="s1">: </span><span class="s2">&quot;Curly&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;BYb&quot;</span><span class="s1">: </span><span class="s2">&quot;Curly&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;bYB&quot;</span><span class="s1">: </span><span class="s2">&quot;Curly&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;YBb&quot;</span><span class="s1">: </span><span class="s2">&quot;Curly&quot;</span><span class="s0">,</span>
            <span class="s2">&quot;YbB&quot;</span><span class="s1">: </span><span class="s2">&quot;Curly&quot;</span><span class="s0">,</span>
        <span class="s1">}</span>
        <span class="s0">return </span><span class="s1">coat_type_mapping.get(dna</span><span class="s0">, </span><span class="s2">&quot;unknown&quot;</span><span class="s1">)</span>

    <span class="s0">def </span><span class="s1">set_sibling(self</span><span class="s0">, </span><span class="s1">sibling):</span>
        <span class="s0">if </span><span class="s1">sibling.name != self.name </span><span class="s0">and </span><span class="s1">sibling.name </span><span class="s0">not in </span><span class="s1">self.siblings:</span>
            <span class="s1">self.siblings.append(sibling.name)</span>
        <span class="s3"># Check if the sibling has a mother or father</span>
        <span class="s0">if </span><span class="s1">sibling.mother:</span>
            <span class="s3"># Add the offspring of the sibling's mother as siblings</span>
            <span class="s0">for </span><span class="s1">offspring </span><span class="s0">in </span><span class="s1">sibling.mother.offspring:</span>
                <span class="s0">if </span><span class="s1">offspring.name != self.name </span><span class="s0">and </span><span class="s1">offspring.name </span><span class="s0">not in </span><span class="s1">self.siblings:</span>
                    <span class="s1">self.siblings.append(offspring.name)</span>
        <span class="s0">if </span><span class="s1">sibling.father:</span>
            <span class="s3"># Add the offspring of the sibling's father as siblings</span>
            <span class="s0">for </span><span class="s1">offspring </span><span class="s0">in </span><span class="s1">sibling.father.offspring:</span>
                <span class="s0">if </span><span class="s1">offspring.name != self.name </span><span class="s0">and </span><span class="s1">offspring.name </span><span class="s0">not in </span><span class="s1">self.siblings:</span>
                    <span class="s1">self.siblings.append(offspring.name)</span>
        <span class="s3"># Check if the current dog has a mother or father</span>
        <span class="s0">if </span><span class="s1">self.mother:</span>
            <span class="s3"># Add the offspring of the mother as siblings</span>
            <span class="s0">for </span><span class="s1">offspring </span><span class="s0">in </span><span class="s1">self.mother.offspring:</span>
                <span class="s0">if </span><span class="s1">offspring.name != self.name </span><span class="s0">and </span><span class="s1">offspring.name </span><span class="s0">not in </span><span class="s1">self.siblings:</span>
                    <span class="s1">self.siblings.append(offspring.name)</span>
        <span class="s0">if </span><span class="s1">self.father:</span>
            <span class="s3"># Add the offspring of the father as siblings</span>
            <span class="s0">for </span><span class="s1">offspring </span><span class="s0">in </span><span class="s1">self.father.offspring:</span>
                <span class="s0">if </span><span class="s1">offspring.name != self.name </span><span class="s0">and </span><span class="s1">offspring.name </span><span class="s0">not in </span><span class="s1">self.siblings:</span>
                    <span class="s1">self.siblings.append(offspring.name)</span>

    <span class="s0">def </span><span class="s1">get_sibling(self):</span>
        <span class="s0">return </span><span class="s1">self.siblings</span>

    <span class="s0">def </span><span class="s1">set_mother(self</span><span class="s0">, </span><span class="s1">mother):</span>
        <span class="s1">self.mother = mother</span>

    <span class="s0">def </span><span class="s1">get_mother(self):</span>
        <span class="s0">return </span><span class="s1">self.mother</span>

    <span class="s0">def </span><span class="s1">getcolor_coat(self):</span>
        <span class="s0">return </span><span class="s1">self.color_coat</span>

    <span class="s0">def </span><span class="s1">set_father(self</span><span class="s0">, </span><span class="s1">father):</span>
        <span class="s1">self.father = father</span>

    <span class="s0">def </span><span class="s1">get_father(self):</span>
        <span class="s0">return </span><span class="s1">self.father</span>

    <span class="s0">def </span><span class="s1">set_offspring(self</span><span class="s0">, </span><span class="s1">offspring):</span>
        <span class="s1">self.offspring.append(offspring)</span>

    <span class="s0">def </span><span class="s1">get_offspring(self):</span>
        <span class="s0">return </span><span class="s1">self.offspring</span>

    <span class="s0">def </span><span class="s1">set_name(self</span><span class="s0">, </span><span class="s1">name):</span>
        <span class="s1">self.name = name</span>

    <span class="s0">def </span><span class="s1">get_name(self):</span>
        <span class="s0">return </span><span class="s1">self.name</span>

    <span class="s0">def </span><span class="s1">breed(self</span><span class="s0">, </span><span class="s1">partner</span><span class="s0">,</span><span class="s1">name=</span><span class="s0">None,</span><span class="s1">repeat=</span><span class="s0">None</span><span class="s1">):</span>
        <span class="s3"># Combine the DNA of the two parents to create the DNA of the offspring</span>
        <span class="s0">try</span><span class="s1">:</span>
            <span class="s3"># Combine the DNA of the two parents to create the DNA of the offspring</span>
            <span class="s0">if </span><span class="s1">self.sex == </span><span class="s2">&quot;Male&quot; </span><span class="s0">and </span><span class="s1">partner.sex == </span><span class="s2">&quot;Male&quot; </span><span class="s0">or </span><span class="s1">self.sex == </span><span class="s2">&quot;Female&quot; </span><span class="s0">and </span><span class="s1">partner.sex == </span><span class="s2">&quot;Female&quot;</span><span class="s1">:</span>
                <span class="s0">raise </span><span class="s1">ValueError(</span><span class="s2">&quot;You can't breed two dogs of the same sex together&quot;</span><span class="s1">)</span>
        <span class="s0">except </span><span class="s1">ValueError </span><span class="s0">as </span><span class="s1">error:</span>
            <span class="s1">print(error)</span>
            <span class="s0">return</span>
        <span class="s0">try</span><span class="s1">:</span>
            <span class="s0">if </span><span class="s2">&quot;R&quot; </span><span class="s0">in </span><span class="s1">self.dna </span><span class="s0">or </span><span class="s2">&quot;R&quot; </span><span class="s0">in </span><span class="s1">partner.dna:</span>
                <span class="s0">raise </span><span class="s1">ValueError(</span><span class="s2">&quot;You can't breed a Retarded &amp; Inbred dog&quot;</span><span class="s1">)</span>
        <span class="s0">except </span><span class="s1">ValueError </span><span class="s0">as </span><span class="s1">error:</span>
            <span class="s1">print(error)</span>
            <span class="s0">return</span>
        <span class="s3"># Create a new Dog object with the mother and father specified</span>
        <span class="s1">offspring = Dog(name</span><span class="s0">, </span><span class="s1">mother=self</span><span class="s0">, </span><span class="s1">father=partner)</span>
        <span class="s3"># Add the offspring to the list of offspring for both the mother and father</span>
        <span class="s1">self.offspring.append(offspring)</span>
        <span class="s1">partner.offspring.append(offspring)</span>

        <span class="s3"># Add the previous offspring of both parents as siblings to the new dog,</span>
        <span class="s3"># excluding the new dog itself</span>
        <span class="s1">siblings = []</span>
        <span class="s0">if </span><span class="s1">partner.mother:</span>
            <span class="s1">siblings += partner.mother.offspring</span>
        <span class="s0">if </span><span class="s1">partner.father:</span>
            <span class="s1">siblings += partner.father.offspring</span>
        <span class="s0">if </span><span class="s1">self.mother:</span>
            <span class="s3"># Add the offspring of the mother as siblings</span>
            <span class="s0">for </span><span class="s1">offspring </span><span class="s0">in </span><span class="s1">self.mother.offspring:</span>
                <span class="s0">if </span><span class="s1">offspring.name != self.name </span><span class="s0">and </span><span class="s1">offspring.name </span><span class="s0">not in </span><span class="s1">self.siblings:</span>
                    <span class="s1">self.siblings.append(offspring.name)</span>
        <span class="s0">if </span><span class="s1">self.father:</span>
            <span class="s3"># Add the offspring of the father as siblings</span>
            <span class="s0">for </span><span class="s1">offspring </span><span class="s0">in </span><span class="s1">self.father.offspring:</span>
                <span class="s0">if </span><span class="s1">offspring.name != self.name </span><span class="s0">and </span><span class="s1">offspring.name </span><span class="s0">not in </span><span class="s1">self.siblings:</span>
                    <span class="s1">self.siblings.append(offspring.name)</span>
        <span class="s0">for </span><span class="s1">sibling </span><span class="s0">in </span><span class="s1">siblings:</span>
            <span class="s0">if </span><span class="s1">sibling != offspring:</span>
                <span class="s1">offspring.set_sibling(sibling)</span>

        <span class="s0">if </span><span class="s1">random.random() &lt; </span><span class="s4">0.1</span><span class="s1">:</span>
            <span class="s1">offspring.mutate()</span>

        <span class="s0">if </span><span class="s1">random.random() &lt; </span><span class="s4">0.3</span><span class="s1">:</span>
            <span class="s1">offspring.inbreeding()</span>

        <span class="s3"># Return the offspring</span>
        <span class="s0">return </span><span class="s1">offspring</span>

    <span class="s0">def </span><span class="s1">mutate(self):</span>
        <span class="s5">&quot;&quot;&quot;Introduce a mutation in the DNA sequence of the dog with a very low probability.&quot;&quot;&quot;</span>
        <span class="s2">&quot;&quot;&quot;Introduce a mutation in the DNA sequence of the dog with a very low probability.&quot;&quot;&quot;</span>
        <span class="s3"># Check if the mutate method has already been called</span>
        <span class="s0">if </span><span class="s1">self.mutated == </span><span class="s0">True</span><span class="s1">:</span>
            <span class="s1">print(</span><span class="s2">&quot;The dog has already mutated. The mutate method can only be called once.&quot;</span><span class="s1">)</span>
            <span class="s0">return</span>

        <span class="s1">dna_sequence = list(self.dna)</span>
        <span class="s1">i = random.randint(</span><span class="s4">0</span><span class="s0">, </span><span class="s1">len(dna_sequence) - </span><span class="s4">3</span><span class="s1">)</span>
        <span class="s1">dna_sequence[i] = self.random_dna_letter()</span>
        <span class="s1">self.dna = </span><span class="s2">&quot;&quot;</span><span class="s1">.join(dna_sequence)</span>
        <span class="s1">self.color_coat = self.dna_to_color_coat(self.dna[:</span><span class="s4">3</span><span class="s1">])</span>
        <span class="s1">self.color_eyes = self.dna_to_color_eyes(self.dna[</span><span class="s4">3</span><span class="s1">:</span><span class="s4">6</span><span class="s1">])</span>
        <span class="s1">self.coat_type = self.dna_to_coat_type(self.dna[</span><span class="s4">6</span><span class="s1">:</span><span class="s4">9</span><span class="s1">])</span>
        <span class="s1">print(</span><span class="s2">f&quot;A random mutation happened during </span><span class="s0">{</span><span class="s1">self.name</span><span class="s0">} </span><span class="s2">breeding&quot;</span><span class="s1">)</span>
        <span class="s1">print(dna_sequence[i]</span><span class="s0">,</span><span class="s2">&quot;at&quot;</span><span class="s0">,</span><span class="s1">i)</span>
        <span class="s1">self.mutated = </span><span class="s0">True</span>

    <span class="s0">def </span><span class="s1">random_dna_letter(self):</span>
        <span class="s5">&quot;&quot;&quot;Return a random letter from the DNA alphabet.&quot;&quot;&quot;</span>
        <span class="s0">return </span><span class="s1">random.choice([</span><span class="s2">&quot;B&quot;</span><span class="s0">, </span><span class="s2">&quot;b&quot;</span><span class="s0">, </span><span class="s2">&quot;Y&quot;</span><span class="s1">])</span>

    <span class="s0">def </span><span class="s1">inbreeding(self):</span>

        <span class="s0">if </span><span class="s1">self.father </span><span class="s0">in </span><span class="s1">self.mother.siblings </span><span class="s0">or </span><span class="s1">self.father </span><span class="s0">in </span><span class="s1">self.mother.offspring </span><span class="s0">or </span><span class="s1">self.mother </span><span class="s0">in </span><span class="s1">self.father.offspring:</span>
            <span class="s1">self.dna += </span><span class="s2">&quot;R&quot;</span>
            <span class="s1">print(</span><span class="s2">&quot;this dog is inbred and retarded&quot;</span><span class="s1">)</span></pre>
</body>
</html>