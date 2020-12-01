from common import audit

if __name__ == '__main__':
    product = audit(r_length=2)
    print(product if product else 'No solution found')
