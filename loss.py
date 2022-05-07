fa_val = np.linalg.norm(fa, 2)
fv_val = np.linalg.norm(fv, 2)
L_sim = np.dot(fa, fv)/max(fa_val*fv_val, eta)

L_ce = 0
for i in range(k):
	L_ce += y[i]*log(1/p[i])

L = L_ce + L_sim