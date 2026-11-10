// payment_dto.ts
export interface PaymentRecord {
  cardholderName: string;
  paymentAccountNumber: string;
  cardExpiryDate: string;
  cvvCode: string;
  paymentAuthorizationRecord: string;
}
