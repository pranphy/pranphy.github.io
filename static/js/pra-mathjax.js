<script type="text/x-mathjax-config">
    MathJax.Hub.Config({
        extensions: ["tex2jax.js"],
        jax: ["input/TeX", "output/HTML-CSS"],
        tex2jax: {
            inlineMath: [ ['$','$'], ["\\(","\\)"] ],
            displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
            processEscapes: true
        },
        TeX: { 
            equationNumbers: { autoNumber: "AMS" },
            extensions: ["AMSmath.js","AMSsymbols.js","autobold.js","cancel.js"]
        },
        "HTML-CSS": { fonts: ["TeX"] }
    });
</script>
<script>
    MathJax.Hub.Config({
      TeX: {
        Macros: {
          RR: "{\\bf R}",
          exp: ["{e^{#1}}",1],
          pdv: ["{\\frac{\\partial^{#1}{ #2 }}{\\partial{ #3 }^{#1}}}", 3,""],
          dv:  ["{\\frac{\\mathrm{d}^{#1}{ #2 }}{\\\mathrm{d}{#3}^{#1}}}", 3,""],
          ket: ["{\\left\\lvert #1\\right\\rangle}",1],
          bra: ["{\\left\\langle #1\\right\\rvert}",1],
          ip:  ["{\\left\\langle #1\vert #2 \\right\\rangle",2],
          slashed:[ "{\\mathord{\\smash{\\mathop{#1\\strut}\\limits^{\\smash{\\textstyle\\lower10pt{\\unicode{x2215}}}}}\\strut}}",1],
        }
      }
    });
</script>

