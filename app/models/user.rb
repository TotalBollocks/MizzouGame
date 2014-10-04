class User < ActiveRecord::Base
  has_secure_password
  has_many :high_scores
  
  validates :username, presence: true, uniqueness: true
  validates :password, presence: true, confirmation: true
  
  def to_s
    username
  end
  
end
