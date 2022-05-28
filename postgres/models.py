from database import Base
from sqlalchemy import String,Boolean,Integer,Float,Column


class Patient(Base):
    __tablename__ ='patients'
    id= Column(Integer,primary_key=True)
    firstname= Column(String(35),nullable=False)
    lastname= Column(String(35),nullable=False)
    gender = Column(String(5),nullable=False)
    age = Column(Float,nullable=False)
    hypertension= Column(Boolean, default=False)
    heart_disease= Column(Boolean, default=False)
    ever_married= Column(String(5),nullable=False)
    work_type=  Column(String(35),nullable=False)
    Residence_type=  Column(String(35),nullable=False)
    avg_glucose_level=Column(Float,nullable=False)
    bmi= Column(Float,nullable=False)
    smoking_status= Column(String(35),nullable=False)

    def __repr__(self):
        return f"<id={self.id} firstname={self.firstname}>" 