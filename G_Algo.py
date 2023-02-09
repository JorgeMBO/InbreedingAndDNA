<html>
<head>
<title>G_Algo.py</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<style type="text/css">
.s0 { color: #cc7832;}
.s1 { color: #a9b7c6;}
.s2 { color: #808080;}
.s3 { color: #6897bb;}
.s4 { color: #629755; font-style: italic;}
.s5 { color: #6a8759;}
</style>
</head>
<body bgcolor="#2b2b2b">
<table CELLSPACING=0 CELLPADDING=5 COLS=1 WIDTH="100%" BGCOLOR="#606060" >
<tr><td><center>
<font face="Arial, Helvetica" color="#000000">
G_Algo.py</font>
</center></td></tr></table>
<pre><span class="s0">import </span><span class="s1">random</span>
<span class="s0">from </span><span class="s1">dogclass </span><span class="s0">import </span><span class="s1">Dog  </span><span class="s2"># Import the Dog class from the dogclass module</span>
<span class="s0">import </span><span class="s1">matplotlib.pyplot </span><span class="s0">as </span><span class="s1">plt</span>
<span class="s0">import </span><span class="s1">random</span>

<span class="s0">class </span><span class="s1">GeneticAlgorithm:</span>
    <span class="s0">def </span><span class="s1">__init__(self</span><span class="s0">, </span><span class="s1">population_size):</span>
        <span class="s1">self.population_size = population_size</span>
        <span class="s1">self.population = []</span>
        <span class="s1">self.generations = </span><span class="s3">0</span>

    <span class="s0">def </span><span class="s1">generate_population(self):</span>
        <span class="s4">&quot;&quot;&quot;Generates a population of random dogs&quot;&quot;&quot;</span>
        <span class="s0">for </span><span class="s1">i </span><span class="s0">in </span><span class="s1">range(self.population_size):</span>
            <span class="s1">dog = Dog()</span>
            <span class="s1">self.population.append(dog)</span>

    <span class="s0">def </span><span class="s1">rank_dogs(self):</span>
        <span class="s4">&quot;&quot;&quot;Ranks the dogs in the population based on their attributes&quot;&quot;&quot;</span>
        <span class="s1">self.population.sort(key=</span><span class="s0">lambda </span><span class="s1">x: x.attribute_score()</span><span class="s0">, </span><span class="s1">reverse=</span><span class="s0">True</span><span class="s1">)</span>

    <span class="s0">def </span><span class="s1">breed_top_dogs(self):</span>
        <span class="s4">&quot;&quot;&quot;Breeds the top 10 dogs in the population&quot;&quot;&quot;</span>
        <span class="s1">top_dogs = self.population[:</span><span class="s3">10</span><span class="s1">]</span>
        <span class="s0">for </span><span class="s1">i </span><span class="s0">in </span><span class="s1">range(</span><span class="s3">0</span><span class="s0">, </span><span class="s1">len(top_dogs)</span><span class="s0">, </span><span class="s3">2</span><span class="s1">):</span>
            <span class="s1">mother = top_dogs[i]</span>
            <span class="s1">father = top_dogs[i+</span><span class="s3">1</span><span class="s1">]</span>
            <span class="s1">child = Dog(mother=mother</span><span class="s0">, </span><span class="s1">father=father)</span>
            <span class="s1">self.population.append(child)</span>

    <span class="s0">def </span><span class="s1">run(self</span><span class="s0">, </span><span class="s1">num_generations):</span>
        <span class="s4">&quot;&quot;&quot;Runs the genetic algorithm for a specified number of generations&quot;&quot;&quot;</span>
        <span class="s1">self.generate_population()</span>
        <span class="s0">for </span><span class="s1">i </span><span class="s0">in </span><span class="s1">range(num_generations):</span>
            <span class="s1">self.rank_dogs()</span>
            <span class="s1">self.breed_top_dogs()</span>
            <span class="s1">self.generations += </span><span class="s3">1</span>
        <span class="s1">print(</span><span class="s5">&quot;Top 3 dogs after {} generations:&quot;</span><span class="s1">.format(self.generations))</span>
        <span class="s0">for </span><span class="s1">i </span><span class="s0">in </span><span class="s1">range(</span><span class="s3">3</span><span class="s1">):</span>
            <span class="s1">self.population[i].attribute_score()</span>
            <span class="s1">print(self.population[i]</span><span class="s0">, </span><span class="s5">&quot;DNA:&quot;</span><span class="s0">,</span><span class="s1">self.population[i].dna)</span>

<span class="s2"># Initialize the genetic algorithm</span>
<span class="s1">ga = GeneticAlgorithm(</span><span class="s3">200</span><span class="s1">)</span>

<span class="s2"># Run the algorithm for 50 generations</span>
<span class="s1">ga.run(</span><span class="s3">2</span><span class="s1">)</span>
</pre>
</body>
</html>