import numpy as np

def parse_file(filename):
    def last_float(st):
        return float(st.split()[-1])

    with open(filename) as f:
        for line in f:
            if line.find('Oracle LL:') != -1:
                oracle_ll = last_float(line)
            elif line.find('Empirical LL:') != -1:
                empirical_ll = last_float(line)
            elif line.find('SRS LL:') != -1:
                srs_ll = last_float(line)
            elif line.find('Second-order LL:') != -1:
                so_ll = last_float(line)
            elif line.find('|| vec(P) - vec(PSO) ||_1') != -1:
                diff_so = last_float(line)
            elif line.find('|| vec(P) - vec(PSRS) ||_1') != -1:
                diff_srs = last_float(line)

        return oracle_ll, empirical_ll, srs_ll, so_ll, diff_so, diff_srs

def collect(dimension, nseq, seq_len, nsim):
    all_oracle_ll = []
    all_empirical_ll = []
    all_srs_ll = []
    all_so_ll = []
    all_diff_so = []
    all_diff_srs = []
    for k in xrange(1, nsim + 1):
        (oracle_ll, empirical_ll, srs_ll,
         so_ll, diff_so, diff_srs) = parse_file('results/sim-%d-%d-%d.%d' % (
                dimension, nseq, seq_len, k))
        all_oracle_ll.append(oracle_ll)
        all_empirical_ll.append(empirical_ll)
        all_srs_ll.append(srs_ll)
        all_so_ll.append(so_ll)
        all_diff_so.append(diff_so)
        all_diff_srs.append(diff_srs)

    def ll_ratios(ll1, ll2):
        num_samp = nseq * (seq_len - 1)
        z = np.array(ll1) - np.array(ll2)
        return np.exp(z / num_samp) - 1

    
    return (ll_ratios(all_srs_ll, all_oracle_ll), ll_ratios(all_empirical_ll, all_oracle_ll),
            ll_ratios(all_so_ll, all_oracle_ll), all_diff_so, all_diff_srs)

if __name__ == '__main__':
    srs_ratios, emp_ratios, so_ratios, all_diff_so, all_diff_srs = collect(2, 20, 80, 20)
    print '2 40 80'
    print 'SRS diff', np.mean(all_diff_srs), np.std(all_diff_srs)
    print 'Empirical diff', np.mean(all_diff_so), np.std(all_diff_so)
    print 'SRS LL ratio', np.mean(srs_ratios), np.std(srs_ratios)
    print 'Empirical LL ratio', np.mean(emp_ratios), np.std(emp_ratios)
    print 'SO markov ratio', np.mean(so_ratios), np.std(so_ratios)
    print '%0.2f$\pm$%0.2f & %0.2f$\pm$%0.2f & %.1e$\pm$%.1e & %.1e$\pm$%.1e & %.1e$\pm$%.1e' % (
        np.mean(all_diff_srs), np.std(all_diff_srs),
        np.mean(all_diff_so), np.std(all_diff_so),
        np.mean(srs_ratios), np.std(srs_ratios),
        np.mean(emp_ratios), np.std(emp_ratios),
        np.mean(so_ratios), np.std(so_ratios),
        )

    srs_ratios, emp_ratios, so_ratios, all_diff_so, all_diff_srs = collect(4, 40, 640, 20)
    print '4 80 640'
    print 'SRS diff', np.mean(all_diff_srs), np.std(all_diff_srs)
    print 'Empirical diff', np.mean(all_diff_so), np.std(all_diff_so)
    print 'SRS LL ratio', np.mean(srs_ratios), np.std(srs_ratios)
    print 'Empirical LL ratio', np.mean(emp_ratios), np.std(emp_ratios)
    print 'SO markov ratio', np.mean(so_ratios), np.std(so_ratios)
    print '%0.2f$\pm$%0.2f & %0.2f$\pm$%0.2f & %.1e$\pm$%.1e & %.1e$\pm$%.1e & %.1e$\pm$%.1e' % (
        np.mean(all_diff_srs), np.std(all_diff_srs),
        np.mean(all_diff_so), np.std(all_diff_so),
        np.mean(srs_ratios), np.std(srs_ratios),
        np.mean(emp_ratios), np.std(emp_ratios),
        np.mean(so_ratios), np.std(so_ratios),
        )

    srs_ratios, emp_ratios, so_ratios, all_diff_so, all_diff_srs = collect(6, 60, 2160, 20)
    print '6 60 2160'
    print 'SRS diff', np.mean(all_diff_srs), np.std(all_diff_srs)
    print 'Empirical diff', np.mean(all_diff_so), np.std(all_diff_so)
    print 'SRS LL ratio', np.mean(srs_ratios), np.std(srs_ratios)
    print 'Empirical LL ratio', np.mean(emp_ratios), np.std(emp_ratios)
    print 'SO markov ratio', np.mean(so_ratios), np.std(so_ratios)
    print '%0.2f$\pm$%0.2f & %0.2f$\pm$%0.2f & %.1e$\pm$%.1e & %.1e$\pm$%.1e & %.1e$\pm$%.1e' % (
        np.mean(all_diff_srs), np.std(all_diff_srs),
        np.mean(all_diff_so), np.std(all_diff_so),
        np.mean(srs_ratios), np.std(srs_ratios),
        np.mean(emp_ratios), np.std(emp_ratios),
        np.mean(so_ratios), np.std(so_ratios),
        )    
