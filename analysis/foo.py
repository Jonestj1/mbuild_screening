rand_n100 =     [x['total'] for n, x in s2.items() if 'n-100' in n and 'rand' in n]
rand_n100_std = [x['err']   for n, x in s2.items() if 'n-100' in n and 'rand' in n]
rand_n81 =      [x['total'] for n, x in s2.items() if 'n-81'  in n and 'rand' in n]
rand_n81_std =  [x['err']   for n, x in s2.items() if 'n-81'  in n and 'rand' in n]
rand_n64 =      [x['total'] for n, x in s2.items() if 'n-64'  in n and 'rand' in n]
rand_n64_std =  [x['err']   for n, x in s2.items() if 'n-64'  in n and 'rand' in n]

grid_n100 =     [x['total'] for n, x in s2.items() if 'n-100' in n and 'grid' in n]
grid_n100_std = [x['err']   for n, x in s2.items() if 'n-100' in n and 'grid' in n]
grid_n81 =      [x['total'] for n, x in s2.items() if 'n-81'  in n and 'grid' in n]
grid_n81_std =  [x['err']   for n, x in s2.items() if 'n-81'  in n and 'grid' in n]
grid_n64 =      [x['total'] for n, x in s2.items() if 'n-64'  in n and 'grid' in n]
grid_n64_std =  [x['err']   for n, x in s2.items() if 'n-64'  in n and 'grid' in n]
