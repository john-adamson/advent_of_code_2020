from common import audit

if __name__ == '__main__':
    product = audit(r_length=3)
    print(product if product else 'No solution found')
