class SessionsController < ApplicationController
  def new
  end
  
  def create
    user = User.find_by(username: params[:username])
    
    if user && user.authenticate(params[:password])
      session[:user_id] = user.id
      flash[:notice] = "You have signed in!"
      redirect_to root_path
    else
      flash.now[:alert] = "Invalid username or password"
      redirect_to :back
    end
  end
  
  def destroy
    flash[:notice] = "You have signed out"
    session[:user_id] = nil
    redirect_to root_path
  end
end
