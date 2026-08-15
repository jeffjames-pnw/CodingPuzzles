# multiply_2_lists [1,2],[3,4,5]

function pretty($result)
{
    if ($result -eq $null) {
        "null"
    } elseif ("$($result.GetType().BaseType)" -eq 'array')
    {
        "[" + (($result | %{ pretty $_ }) -join ',') + "]"
    } else { "$result" }
}

function multiply_2_lists($left, $right)
{
    $result = @()
    foreach ($l in $left)
    {
        foreach ($r in $right)
        {
            $result += ,@($l, $r)
        }
    }
    $result
}

function multiply_n_lists($in)
{
    $out = $in[0] | %{ ,@($_) }
    foreach ($aa in $in[1..$in.Length])
    {
        $oa = @()
        foreach ($a in $aa)
        {
            $oa += $out | %{ ,@(@($_)+$a) }
        }
        $out = $oa
    }
    return $out
}

pretty (multiply_2_lists @(1,2) @(3,4,5))
pretty (multiply_n_lists @(,@(1,2),@(3,4,5)))
pretty (multiply_n_lists @(,@(1,2),@(3,4,5),@(6,7)))